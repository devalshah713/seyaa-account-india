"""Read every tab of the Diamond Issue Jangad workbook into flat rows."""
import re, zipfile
from xml.etree import ElementTree as ET

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

def load(path='issue.xlsx'):
    z = zipfile.ZipFile(path)
    ss = [''.join(t.text or '' for t in si.iter(f'{NS}t'))
          for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(f'{NS}si')]
    names = [s.get('name') for s in ET.fromstring(z.read('xl/workbook.xml')).iter(f'{NS}sheet')]
    sheets = {}
    for i, name in enumerate(names, start=1):
        sh = ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'))
        rows = {}
        for c in sh.iter(f'{NS}c'):
            col, rn = re.match(r'([A-Z]+)(\d+)', c.get('r')).groups()
            v = c.find(f'{NS}v')
            if v is None:
                continue
            val = ss[int(v.text)] if c.get('t') == 's' else v.text
            if val is None or str(val).strip() == '':
                continue
            rows.setdefault(int(rn), {})[col] = str(val).strip()
        sheets[name] = rows
    return sheets

def header_of(rows):
    """Find the header row and map label -> column letter."""
    for rn in sorted(rows)[:6]:
        labels = {re.sub(r'\s+', ' ', v).strip().upper(): c for c, v in rows[rn].items()}
        if 'DESIGN NUMBER' in labels:
            return rn, labels
    return None, {}

def flat(path='issue.xlsx'):
    """Yield dicts with sheet, row, design, sub, shape, size, pcs — design and sub
    carried down, as these sheets leave them blank on continuation rows."""
    for sheet, rows in load(path).items():
        hrn, labels = header_of(rows)
        if hrn is None:
            continue
        def col(*names):
            for n in names:
                for label, c in labels.items():
                    if label == n:
                        return c
            for n in names:
                for label, c in labels.items():
                    if n in label:
                        return c
            return None
        c_design = col('DESIGN NUMBER')
        c_sub = col('SUB DESIGN NO', 'SUB DESING NO', 'SUB DESIGN CATEGORY')
        c_shape = col('DIAMOND SHAPE')
        c_size = col('DIAMOND SIZE')
        c_pcs = col('DIAMOND PCS')
        last_design = last_sub = None
        for rn in sorted(rows):
            if rn <= hrn:
                continue
            r = rows[rn]
            design = r.get(c_design) if c_design else None
            sub = r.get(c_sub) if c_sub else None
            if design:
                last_design, last_sub = design, sub
            elif sub:
                last_sub = sub
            yield {
                'sheet': sheet, 'row': rn,
                'design': design or last_design,
                'sub': sub if sub else (last_sub if not design else sub),
                'own_design': design, 'own_sub': sub,
                'shape': r.get(c_shape) if c_shape else None,
                'size': r.get(c_size) if c_size else None,
                'pcs': r.get(c_pcs) if c_pcs else None,
            }
