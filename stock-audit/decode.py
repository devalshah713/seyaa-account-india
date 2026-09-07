#!/usr/bin/env python3
"""
Decode a Google Drive MCP download result into a usable .xlsx.

The Drive connector returns the workbook as base64 inside a JSON envelope, and for a
sheet this size the harness saves that envelope to a file rather than returning it
inline. This turns that file into a real .xlsx on disk, so nothing large has to pass
through the conversation.

    python3 stock-audit/decode.py <tool-result.txt> <out.xlsx>
"""
import base64, json, sys

if len(sys.argv) != 3:
    sys.exit(__doc__)

src, dst = sys.argv[1], sys.argv[2]
with open(src) as fh:
    payload = json.load(fh)

# download_file_content -> {content: <base64>}; some results nest it differently
blob = payload.get("content") or payload.get("fileContent")
if not blob:
    sys.exit(f"No 'content' field in {src}. Keys present: {list(payload)}")

raw = base64.b64decode(blob)
with open(dst, "wb") as fh:
    fh.write(raw)

if raw[:2] != b"PK":
    sys.exit(f"Decoded {len(raw)} bytes but this is not a .xlsx (no PK header). "
             f"Was the export mime type set to the xlsx type?")

print(f"{payload.get('title', '?')} -> {dst} ({len(raw):,} bytes)")
