# India stock sheet — full backlog audit

Generated 2026-09-07 against both sheets as they stood that day. This is the
**historical backlog**, not a daily batch — the twice-daily checks start from this
point and report only what changes after it.

Reference rows `S1805C` (NEW), `A0945` and `A0946` (OLD) were used to calibrate;
they come back clean apart from the A0946 date question noted in the checklist.

Work through it with Deval. Rules: `team/checklists/india-stock-sheet.md`.

---

## NEW — Stock Sheet of Seyaa Factory for India

Scope: full sheet. 1833 stock rows in sheet.
New since last run: S0001C, S0002C, S0003C, S0004C, S0005C, S0006C, S0007C, S0008C, S0009, S0010, S0011C, S0012C, S0013C, S0014C, S0015C, S0016C, S0017C, S0018C, S0019C, S0020C ...

## Errors (194)

| Stock # | Cell | Problem |
|---|---|---|
| S0108 | S109 | Sieve / Size blank while TDW > 0 |
| S0250C | U251 | Product Code blank while TDW = 5.12 |
| S0250C | V251 | Diamond price ($) is hardcoded '=M251*250' — must VLOOKUP the Price List via the product code |
| S0250C | Z251 | Diamond price (₹) is hardcoded '=M251*27000' — must VLOOKUP the Price List via the product code |
| S0364C | J365 | Ring size 'US 10.5' has a space — expected 'US10.5' |
| S0549 | L550 | TDW = 0 but net 0.6346 != gross 1.2346. With no diamonds they should be equal |
| S0550 | L551 | TDW = 0 but net 0.6372 != gross 1.2372. With no diamonds they should be equal |
| S0551 | L552 | TDW = 0 but net 0.605 != gross 1.205. With no diamonds they should be equal |
| S0552 | L553 | TDW = 0 but net 0.6303 != gross 1.2303. With no diamonds they should be equal |
| S0553 | L554 | TDW = 0 but net 0.6367 != gross 1.2367. With no diamonds they should be equal |
| S0554 | L555 | TDW = 0 but net 0.6036 != gross 1.2036. With no diamonds they should be equal |
| S0555 | L556 | TDW = 0 but net 0.6115 != gross 1.2115. With no diamonds they should be equal |
| S0556 | L557 | TDW = 0 but net 0.4956 != gross 1.2956. With no diamonds they should be equal |
| S0557 | L558 | TDW = 0 but net 0.5537 != gross 1.3537. With no diamonds they should be equal |
| S0558 | L559 | TDW = 0 but net 0.5475 != gross 1.3475. With no diamonds they should be equal |
| S0559 | L560 | TDW = 0 but net 0.5545 != gross 1.3545. With no diamonds they should be equal |
| S0560 | L561 | TDW = 0 but net 0.5541 != gross 1.3541. With no diamonds they should be equal |
| S0561 | L562 | TDW = 0 but net 0.5473 != gross 1.3473. With no diamonds they should be equal |
| S0562 | L563 | TDW = 0 but net 0.5421 != gross 1.3421. With no diamonds they should be equal |
| S0563 | L564 | TDW = 0 but net 0.4969 != gross 1.0969. With no diamonds they should be equal |
| S0564 | L565 | TDW = 0 but net 0.4975 != gross 1.0975. With no diamonds they should be equal |
| S0565 | L566 | TDW = 0 but net 0.5322 != gross 1.1322. With no diamonds they should be equal |
| S0566 | L567 | TDW = 0 but net 0.5185 != gross 1.1185. With no diamonds they should be equal |
| S0567 | L568 | TDW = 0 but net 0.5082 != gross 1.1082. With no diamonds they should be equal |
| S0568 | L569 | TDW = 0 but net 0.5033 != gross 1.1033. With no diamonds they should be equal |
| S0569 | L570 | TDW = 0 but net 0.468 != gross 1.068. With no diamonds they should be equal |
| S0644C | U645 | Product Code blank while TDW = 5.12 |
| S0644C | V645 | Diamond price ($) is hardcoded '=M645*250' — must VLOOKUP the Price List via the product code |
| S0644C | Z645 | Diamond price (₹) is hardcoded '=M645*27000' — must VLOOKUP the Price List via the product code |
| S0645C | U646 | Product Code blank while TDW = 5.08 |
| S0645C | V646 | Diamond price ($) is hardcoded '=M646*250' — must VLOOKUP the Price List via the product code |
| S0645C | Z646 | Diamond price (₹) is hardcoded '=M646*27000' — must VLOOKUP the Price List via the product code |
| S0652C | U653 | Product Code blank while TDW = 4.81 |
| S0652C | V653 | Diamond price ($) is hardcoded '=M653*250' — must VLOOKUP the Price List via the product code |
| S0652C | Z653 | Diamond price (₹) is hardcoded '=M653*27000' — must VLOOKUP the Price List via the product code |
| S0653C | U654 | Product Code blank while TDW = 4.9 |
| S0653C | V654 | Diamond price ($) is hardcoded '=M654*250' — must VLOOKUP the Price List via the product code |
| S0653C | Z654 | Diamond price (₹) is hardcoded '=M654*27000' — must VLOOKUP the Price List via the product code |
| S0901C | N902 | Single row: breakup 2.02 != TDW 2.08 |
| S0995 | L996 | NET WEIGHT blank |
| S1060C | U1061 | Product Code blank while TDW = 5.16 |
| S1060C | V1061 | Diamond price ($) is hardcoded '=M1061*250' — must VLOOKUP the Price List via the product code |
| S1060C | Z1061 | Diamond price (₹) is hardcoded '=M1061*27000' — must VLOOKUP the Price List via the product code |
| S1063 | L1064 | Net 4.92 equals gross 4.92 while TDW = 4.4. With diamonds set, net must be less than gross |
| S1220 | L1221 | Net 6.521 equals gross 6.521 while TDW = 5.31. With diamonds set, net must be less than gross |
| S1250C | D1251 | Design Number blank while TDW = 10.26 (>0, so it is compulsory) |
| S1320C | N1321 | Single row: breakup 1.14 != TDW 1.41 |
| S1331C | S1332 | Sieve / Size blank while TDW > 0 |
| S1536C | J1537 | INCH SIZE blank (only earrings/studs may be blank or NA) |
| S1590 | V1591 | Diamond price ($) is a typed value 0.0, not a formula |
| S1590 | Z1591 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1591 | V1592 | Diamond price ($) is a typed value 0.0, not a formula |
| S1591 | Z1592 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1592 | V1593 | Diamond price ($) is a typed value 0.0, not a formula |
| S1592 | Z1593 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1593 | V1594 | Diamond price ($) is a typed value 0.0, not a formula |
| S1593 | Z1594 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1594 | V1595 | Diamond price ($) is a typed value 0.0, not a formula |
| S1594 | Z1595 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1688C | U1689 | Product Code blank while TDW = 3.11 |
| S1727 | V1728 | Diamond price ($) is a typed value 0.0, not a formula |
| S1727 | Z1728 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1728 | V1729 | Diamond price ($) is a typed value 0.0, not a formula |
| S1728 | Z1729 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1729 | V1730 | Diamond price ($) is a typed value 0.0, not a formula |
| S1729 | Z1730 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1730 | V1731 | Diamond price ($) is a typed value 0.0, not a formula |
| S1730 | Z1731 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1731C | V1732 | Diamond price ($) is a typed value 0.0, not a formula |
| S1731C | Z1732 | Diamond price (₹) is a typed value 0.0, not a formula |
| S1815 | A1816 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1816 | A1817 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1817 | A1818 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1818 | A1819 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1819 | A1820 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1820 | A1821 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1821 | A1822 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1822 | A1823 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1823 | A1824 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1824 | A1825 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1825 | A1826 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1826 | A1827 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1827 | A1828 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1828 | A1829 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1829 | A1830 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1830 | A1831 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1831 | A1832 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1832 | A1833 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1833 | A1834 | Row has a Sr number but is otherwise empty (date, design, location, gold, gross, net, party all blank) |
| S1603C/S1604 | U1155 | Multi Product Code blank while a diamond price is present |
| S1603C/S1604 | V1155 | Multi diamond price ($) hardcoded '=M1155*250' — must VLOOKUP the Price List via the product code |
| S1603C/S1604 | Z1155 | Multi diamond price (₹) hardcoded '=M1155*27000' — must VLOOKUP the Price List via the product code |
| S1605C/S1606 | U1157 | Multi Product Code blank while a diamond price is present |
| S1605C/S1606 | V1157 | Multi diamond price ($) hardcoded '=M1157*250' — must VLOOKUP the Price List via the product code |
| S1605C/S1606 | Z1157 | Multi diamond price (₹) hardcoded '=M1157*27000' — must VLOOKUP the Price List via the product code |
| S1607C/S1608 | U1159 | Multi Product Code blank while a diamond price is present |
| S1607C/S1608 | V1159 | Multi diamond price ($) hardcoded '=M1159*250' — must VLOOKUP the Price List via the product code |
| S1607C/S1608 | Z1159 | Multi diamond price (₹) hardcoded '=M1159*27000' — must VLOOKUP the Price List via the product code |
| S1609C/S1610 | U1161 | Multi Product Code blank while a diamond price is present |
| S1609C/S1610 | V1161 | Multi diamond price ($) hardcoded '=M1161*250' — must VLOOKUP the Price List via the product code |
| S1609C/S1610 | Z1161 | Multi diamond price (₹) hardcoded '=M1161*27000' — must VLOOKUP the Price List via the product code |
| S1611C/S1612 | U1163 | Multi Product Code blank while a diamond price is present |
| S1611C/S1612 | V1163 | Multi diamond price ($) hardcoded '=M1163*250' — must VLOOKUP the Price List via the product code |
| S1611C/S1612 | Z1163 | Multi diamond price (₹) hardcoded '=M1163*27000' — must VLOOKUP the Price List via the product code |
| S1613C/S1614 | U1165 | Multi Product Code blank while a diamond price is present |
| S1613C/S1614 | V1165 | Multi diamond price ($) hardcoded '=M1165*250' — must VLOOKUP the Price List via the product code |
| S1613C/S1614 | Z1165 | Multi diamond price (₹) hardcoded '=M1165*27000' — must VLOOKUP the Price List via the product code |
| S1615C/S1616 | U1167 | Multi Product Code blank while a diamond price is present |
| S1615C/S1616 | V1167 | Multi diamond price ($) hardcoded '=M1167*250' — must VLOOKUP the Price List via the product code |
| S1615C/S1616 | Z1167 | Multi diamond price (₹) hardcoded '=M1167*27000' — must VLOOKUP the Price List via the product code |
| S1617C/S1618 | U1169 | Multi Product Code blank while a diamond price is present |
| S1617C/S1618 | V1169 | Multi diamond price ($) hardcoded '=M1169*250' — must VLOOKUP the Price List via the product code |
| S1617C/S1618 | Z1169 | Multi diamond price (₹) hardcoded '=M1169*27000' — must VLOOKUP the Price List via the product code |
| S1619C/S1620 | U1171 | Multi Product Code blank while a diamond price is present |
| S1619C/S1620 | V1171 | Multi diamond price ($) hardcoded '=M1171*250' — must VLOOKUP the Price List via the product code |
| S1619C/S1620 | Z1171 | Multi diamond price (₹) hardcoded '=M1171*27000' — must VLOOKUP the Price List via the product code |
| S1621C/S1622 | U1173 | Multi Product Code blank while a diamond price is present |
| S1621C/S1622 | V1173 | Multi diamond price ($) hardcoded '=M1173*250' — must VLOOKUP the Price List via the product code |
| S1621C/S1622 | Z1173 | Multi diamond price (₹) hardcoded '=M1173*27000' — must VLOOKUP the Price List via the product code |
| S1623C/S1624 | U1175 | Multi Product Code blank while a diamond price is present |
| S1623C/S1624 | V1175 | Multi diamond price ($) hardcoded '=M1175*250' — must VLOOKUP the Price List via the product code |
| S1623C/S1624 | Z1175 | Multi diamond price (₹) hardcoded '=M1175*27000' — must VLOOKUP the Price List via the product code |
| S1625C/S1626 | U1177 | Multi Product Code blank while a diamond price is present |
| S1625C/S1626 | V1177 | Multi diamond price ($) hardcoded '=M1177*250' — must VLOOKUP the Price List via the product code |
| S1625C/S1626 | Z1177 | Multi diamond price (₹) hardcoded '=M1177*27000' — must VLOOKUP the Price List via the product code |
| S1627C/S1628 | U1179 | Multi Product Code blank while a diamond price is present |
| S1627C/S1628 | V1179 | Multi diamond price ($) hardcoded '=M1179*250' — must VLOOKUP the Price List via the product code |
| S1627C/S1628 | Z1179 | Multi diamond price (₹) hardcoded '=M1179*27000' — must VLOOKUP the Price List via the product code |
| S1629C/S1630 | U1181 | Multi Product Code blank while a diamond price is present |
| S1629C/S1630 | V1181 | Multi diamond price ($) hardcoded '=M1181*250' — must VLOOKUP the Price List via the product code |
| S1629C/S1630 | Z1181 | Multi diamond price (₹) hardcoded '=M1181*27000' — must VLOOKUP the Price List via the product code |
| S1631C/S1632 | U1183 | Multi Product Code blank while a diamond price is present |
| S1631C/S1632 | V1183 | Multi diamond price ($) hardcoded '=M1183*250' — must VLOOKUP the Price List via the product code |
| S1631C/S1632 | Z1183 | Multi diamond price (₹) hardcoded '=M1183*27000' — must VLOOKUP the Price List via the product code |
| S1633C/S1634 | U1185 | Multi Product Code blank while a diamond price is present |
| S1633C/S1634 | V1185 | Multi diamond price ($) hardcoded '=M1185*250' — must VLOOKUP the Price List via the product code |
| S1633C/S1634 | Z1185 | Multi diamond price (₹) hardcoded '=M1185*27000' — must VLOOKUP the Price List via the product code |
| S1635C/S1636 | U1187 | Multi Product Code blank while a diamond price is present |
| S1635C/S1636 | V1187 | Multi diamond price ($) hardcoded '=M1187*250' — must VLOOKUP the Price List via the product code |
| S1635C/S1636 | Z1187 | Multi diamond price (₹) hardcoded '=M1187*27000' — must VLOOKUP the Price List via the product code |
| S1637C/S1638 | U1189 | Multi Product Code blank while a diamond price is present |
| S1637C/S1638 | V1189 | Multi diamond price ($) hardcoded '=M1189*250' — must VLOOKUP the Price List via the product code |
| S1637C/S1638 | Z1189 | Multi diamond price (₹) hardcoded '=M1189*27000' — must VLOOKUP the Price List via the product code |
| S1639C/S1640 | U1191 | Multi Product Code blank while a diamond price is present |
| S1639C/S1640 | V1191 | Multi diamond price ($) hardcoded '=M1191*250' — must VLOOKUP the Price List via the product code |
| S1639C/S1640 | Z1191 | Multi diamond price (₹) hardcoded '=M1191*27000' — must VLOOKUP the Price List via the product code |
| S1641C/S1642 | U1193 | Multi Product Code blank while a diamond price is present |
| S1641C/S1642 | V1193 | Multi diamond price ($) hardcoded '=M1193*250' — must VLOOKUP the Price List via the product code |
| S1641C/S1642 | Z1193 | Multi diamond price (₹) hardcoded '=M1193*27000' — must VLOOKUP the Price List via the product code |
| S1708C/S1709 | U1279 | Multi Product Code blank while a diamond price is present |
| S1708C/S1709 | V1279 | Multi diamond price ($) hardcoded '=M1279*250' — must VLOOKUP the Price List via the product code |
| S1708C/S1709 | Z1279 | Multi diamond price (₹) hardcoded '=M1279*27000' — must VLOOKUP the Price List via the product code |
| S1710C/S1711 | U1281 | Multi Product Code blank while a diamond price is present |
| S1710C/S1711 | V1281 | Multi diamond price ($) hardcoded '=M1281*250' — must VLOOKUP the Price List via the product code |
| S1710C/S1711 | Z1281 | Multi diamond price (₹) hardcoded '=M1281*27000' — must VLOOKUP the Price List via the product code |
| S0021C | M22 | STOCK TDW 46.24 != sum of Multi breakup 46.230 (difference +0.010) |
| S0071 | S72 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0072 | S73 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0086C | S87 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0209C | M210 | STOCK TDW 3.59 != sum of Multi breakup 3.610 (difference -0.020) |
| S0236 | M237 | STOCK TDW 2.4 != sum of Multi breakup 2.480 (difference -0.080) |
| S0237 | M238 | STOCK TDW 4.3 != sum of Multi breakup 4.320 (difference -0.020) |
| S0240 | S241 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0241 | S242 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0242 | S243 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0243 | S244 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S0251C | M252 | STOCK TDW 2.39 != sum of Multi breakup 2.810 (difference -0.420) |
| S0256 | M257 | STOCK TDW 25.71 != sum of Multi breakup 25.720 (difference -0.010) |
| S0417 | M418 | STOCK TDW 5.05 != sum of Multi breakup 5.110 (difference -0.060) |
| S0646C | B660 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0647 | B662 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0648C | B664 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0655C | B687 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0663C | B689 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0664C | B702 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0665C | B705 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S0667C | M668 | STOCK TDW 4.13 != sum of Multi breakup 4.120 (difference +0.010) |
| S0667C | B708 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| S1232C | B907 | Multi date 2025-08-08 != STOCK date 2026-07-08 |
| S1233C | B910 | Multi date 2026-08-08 != STOCK date 2026-07-08 |
| S1241C | B915 | Multi date 2026-07-08 != STOCK date 2026-08-08 |
| S1252 | S1253 | Marked MIX on STOCK but there is no Multi group for this Sr |
| S1348 | M1349 | STOCK TDW 7.01 != sum of Multi breakup 6.960 (difference +0.050) |
| S1528C | M1529 | STOCK TDW 3.83 != sum of Multi breakup 3.840 (difference -0.010) |
| S1541C | M1542 | STOCK TDW 2.52 != sum of Multi breakup 2.560 (difference -0.040) |
| S1678C | M1679 | STOCK TDW 2.63 != sum of Multi breakup 2.660 (difference -0.030) |
| S1701C | B1219 | Multi date 2026-03-09 != STOCK date 2026-02-09 |
| S1704C | P1705 | STOCK total pcs 175 != sum of Multi pcs 193 |
| S1705C | P1706 | STOCK total pcs 175 != sum of Multi pcs 193 |
| S1708C | B1279 | Multi date 2026-08-31 != STOCK date 2026-02-09 |
| S1709 | B1279 | Multi date 2026-08-31 != STOCK date 2026-02-09 |
| S1710C | B1281 | Multi date 2026-08-31 != STOCK date 2026-02-09 |
| S1711 | B1281 | Multi date 2026-08-31 != STOCK date 2026-02-09 |
| S1732C | M1733 | STOCK TDW 5.528 != sum of Multi breakup 5.510 (difference +0.018) |

## Summary by rule

| Count | Rule |
|---|---|
| 44 | Multi diamond price |
| 32 | Diamond price |
| 22 | Multi Product Code blank while a diamond price is present |
| 21 | TDW = 0 but net 0 |
| 19 | Row has a Sr number but is otherwise empty |
| 8 | Marked MIX on STOCK but there is no Multi group for this Sr |
| 8 | Multi date 2026-06-16 != STOCK date 2026-07-16 |
| 4 | Product Code blank while TDW = 5 |
| 4 | STOCK TDW 2 |
| 4 | Multi date 2026-08-31 != STOCK date 2026-02-09 |
| 2 | Sieve / Size blank while TDW > 0 |
| 2 | Product Code blank while TDW = 4 |
| 2 | STOCK TDW 3 |
| 2 | STOCK TDW 4 |
| 2 | STOCK TDW 5 |
| 2 | STOCK total pcs 175 != sum of Multi pcs 193 |
| 1 | Ring size 'US 10 |
| 1 | Single row: breakup 2 |
| 1 | NET WEIGHT blank |
| 1 | Net 4 |
| 1 | Net 6 |
| 1 | Design Number blank while TDW = 10 |
| 1 | Single row: breakup 1 |
| 1 | INCH SIZE blank |
| 1 | Product Code blank while TDW = 3 |
| 1 | STOCK TDW 46 |
| 1 | STOCK TDW 25 |
| 1 | Multi date 2025-08-08 != STOCK date 2026-07-08 |
| 1 | Multi date 2026-08-08 != STOCK date 2026-07-08 |
| 1 | Multi date 2026-07-08 != STOCK date 2026-08-08 |
| 1 | STOCK TDW 7 |
| 1 | Multi date 2026-03-09 != STOCK date 2026-02-09 |

## Questions for Deval (3)

| Stock # | Cell | Question |
|---|---|---|
| ALL | Price List B68 | The B-column price list is exactly full to row 68, the same row every VLOOKUP caps at. The next code added lands outside the range. Extend the ranges before adding one? |
| ALL | Price List J68 | The J-column price list is exactly full to row 68, the same row every VLOOKUP caps at. The next code added lands outside the range. Extend the ranges before adding one? |
| S0678 | H679 | Location '784.0' is not in the allowed list. New location, or a typo? |

---

## OLD — Stock Sheet New For India

Scope: full sheet. 4958 stock rows in sheet.
New since last run: 100, 1000, 1001, 1002, 1005, 1006, 1007, 1008, 1009, 101, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019 ...

## Errors (3142)

| Stock # | Cell | Problem |
|---|---|---|
| 4 | D2 | Design Number blank while TDW = 7.38 (>0, so it is compulsory) |
| 4 | H2 | GROSS WEIGHT is zero |
| 5 | H3 | GROSS WEIGHT is zero |
| 6 | D4 | Design Number blank while TDW = 6.18 (>0, so it is compulsory) |
| 6 | H4 | GROSS WEIGHT is zero |
| 7 | D5 | Design Number blank while TDW = 6.21 (>0, so it is compulsory) |
| 7 | H5 | GROSS WEIGHT is zero |
| 8 | D6 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 8 | H6 | GROSS WEIGHT is zero |
| 9 | D7 | Design Number blank while TDW = 5.32 (>0, so it is compulsory) |
| 9 | H7 | GROSS WEIGHT is zero |
| 11 | D8 | Design Number blank while TDW = 5.68 (>0, so it is compulsory) |
| 12 | D9 | Design Number blank while TDW = 5.66 (>0, so it is compulsory) |
| 13 | D10 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 14 | D11 | Design Number blank while TDW = 7.39 (>0, so it is compulsory) |
| 15 | D12 | Design Number blank while TDW = 5.82 (>0, so it is compulsory) |
| 16 | D13 | Design Number blank while TDW = 7.57 (>0, so it is compulsory) |
| 17 | D14 | Design Number blank while TDW = 2.94 (>0, so it is compulsory) |
| 17 | H14 | GROSS WEIGHT is zero |
| 18 | D15 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 19 | D16 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 20 | D17 | Design Number blank while TDW = 5.16 (>0, so it is compulsory) |
| 21 | D18 | Design Number blank while TDW = 3.16 (>0, so it is compulsory) |
| 22 | D19 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 23 | D20 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 24 | D21 | Design Number blank while TDW = 5.15 (>0, so it is compulsory) |
| 25 | D22 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 26 | D23 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 27 | D24 | Design Number blank while TDW = 5.22 (>0, so it is compulsory) |
| 28 | D25 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 29 | D26 | Design Number blank while TDW = 5.17 (>0, so it is compulsory) |
| 30 | D27 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 31 | D28 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 32 | D29 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 33 | D30 | Design Number blank while TDW = 10.08 (>0, so it is compulsory) |
| 34 | D31 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 35 | D32 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 36 | D33 | Design Number blank while TDW = 7.04 (>0, so it is compulsory) |
| 37 | D34 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 38 | D35 | Design Number blank while TDW = 2.94 (>0, so it is compulsory) |
| 39 | D36 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 40 | D37 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 41 | D38 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 42 | D39 | Design Number blank while TDW = 4.85 (>0, so it is compulsory) |
| 43 | D40 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 44 | D41 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 45 | D42 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 46 | D43 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 47 | D44 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 48 | D45 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 49 | D46 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 50 | D47 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 51 | D48 | Design Number blank while TDW = 5.28 (>0, so it is compulsory) |
| 52 | D49 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 53 | D50 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 55 | D51 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 56 | D52 | Design Number blank while TDW = 4.92 (>0, so it is compulsory) |
| 57 | D53 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 58 | D54 | Design Number blank while TDW = 4.89 (>0, so it is compulsory) |
| 59 | D55 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 60 | D56 | Design Number blank while TDW = 7.07 (>0, so it is compulsory) |
| 61 | D57 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 62 | D58 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 63 | D59 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 64 | D60 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 65 | D61 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 66 | D62 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 67 | D63 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 68 | D64 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 69 | D65 | Design Number blank while TDW = 2.95 (>0, so it is compulsory) |
| 70 | D66 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 71 | D67 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 72 | D68 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 73 | D69 | Design Number blank while TDW = 8.31 (>0, so it is compulsory) |
| 74 | D70 | Design Number blank while TDW = 23.04 (>0, so it is compulsory) |
| 75 | D71 | Design Number blank while TDW = 2.93 (>0, so it is compulsory) |
| 76 | D72 | Design Number blank while TDW = 2.97 (>0, so it is compulsory) |
| 54 | D73 | Design Number blank while TDW = 5.26 (>0, so it is compulsory) |
| 77 | D74 | Design Number blank while TDW = 2.9 (>0, so it is compulsory) |
| 78 | D75 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 79 | D76 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 80 | D77 | Design Number blank while TDW = 5.26 (>0, so it is compulsory) |
| 81 | D78 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 82 | D79 | Design Number blank while TDW = 7.04 (>0, so it is compulsory) |
| 83 | D80 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 84 | D81 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 85 | D82 | Design Number blank while TDW = 7.03 (>0, so it is compulsory) |
| 86 | D83 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 87 | D84 | Design Number blank while TDW = 7.04 (>0, so it is compulsory) |
| 88 | D85 | Design Number blank while TDW = 7.09 (>0, so it is compulsory) |
| 89 | D86 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 90 | D87 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 91 | D88 | Design Number blank while TDW = 10.07 (>0, so it is compulsory) |
| 92 | D89 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 93 | D90 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 94 | D91 | Design Number blank while TDW = 10.02 (>0, so it is compulsory) |
| 95 | D92 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 96 | D93 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 97 | D94 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 98 | D95 | Design Number blank while TDW = 2.97 (>0, so it is compulsory) |
| 99 | D96 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 100 | D97 | Design Number blank while TDW = 2.97 (>0, so it is compulsory) |
| 101 | D98 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 102 | D99 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 103 | D100 | Design Number blank while TDW = 3.0 (>0, so it is compulsory) |
| 104 | D101 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 105 | D102 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 106 | D103 | Design Number blank while TDW = 3.02 (>0, so it is compulsory) |
| 107 | D104 | Design Number blank while TDW = 2.97 (>0, so it is compulsory) |
| 108 | D105 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 109 | D106 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 110 | D107 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 111 | D108 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 112 | D109 | Design Number blank while TDW = 7.09 (>0, so it is compulsory) |
| 113 | D110 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 114 | D111 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 115 | D112 | Design Number blank while TDW = 7.09 (>0, so it is compulsory) |
| 116 | D113 | Design Number blank while TDW = 7.06 (>0, so it is compulsory) |
| 117 | D114 | Design Number blank while TDW = 7.07 (>0, so it is compulsory) |
| 118 | D115 | Design Number blank while TDW = 6.99 (>0, so it is compulsory) |
| 119 | D116 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 120 | D117 | Design Number blank while TDW = 7.07 (>0, so it is compulsory) |
| 121 | D118 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 122 | D119 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 123 | D120 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 124 | D121 | Design Number blank while TDW = 10.07 (>0, so it is compulsory) |
| 125 | D122 | Design Number blank while TDW = 10.07 (>0, so it is compulsory) |
| 126 | D123 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 127 | D124 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 128 | D125 | Design Number blank while TDW = 10.02 (>0, so it is compulsory) |
| 129 | D126 | Design Number blank while TDW = 10.12 (>0, so it is compulsory) |
| 130 | D127 | Design Number blank while TDW = 10.02 (>0, so it is compulsory) |
| 131 | D128 | Design Number blank while TDW = 10.08 (>0, so it is compulsory) |
| 132 | D129 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 133 | D130 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 134 | D131 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 135 | D132 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 136 | D133 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 137 | D134 | Design Number blank while TDW = 7.03 (>0, so it is compulsory) |
| 138 | D135 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 139 | D136 | Design Number blank while TDW = 7.04 (>0, so it is compulsory) |
| 140 | D137 | Design Number blank while TDW = 5.26 (>0, so it is compulsory) |
| 141 | D138 | Design Number blank while TDW = 5.28 (>0, so it is compulsory) |
| 142 | D139 | Design Number blank while TDW = 5.26 (>0, so it is compulsory) |
| 143 | D140 | Design Number blank while TDW = 5.31 (>0, so it is compulsory) |
| 144 | D141 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 145 | D142 | Design Number blank while TDW = 5.29 (>0, so it is compulsory) |
| 146 | D143 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 147 | D144 | Design Number blank while TDW = 5.29 (>0, so it is compulsory) |
| 148 | D145 | Design Number blank while TDW = 5.29 (>0, so it is compulsory) |
| 149 | D146 | Design Number blank while TDW = 5.3 (>0, so it is compulsory) |
| 150 | D147 | Design Number blank while TDW = 5.26 (>0, so it is compulsory) |
| 151 | D148 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 152 | D149 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 153 | D150 | Design Number blank while TDW = 7.03 (>0, so it is compulsory) |
| 154 | D151 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 155 | D152 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 156 | D153 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 157 | D154 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 158 | D155 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 159 | D156 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 160 | D157 | Design Number blank while TDW = 5.31 (>0, so it is compulsory) |
| 161 | D158 | Design Number blank while TDW = 5.24 (>0, so it is compulsory) |
| 162 | D159 | Design Number blank while TDW = 5.35 (>0, so it is compulsory) |
| 163 | D160 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 164 | D161 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 165 | D162 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 166 | D163 | Design Number blank while TDW = 5.31 (>0, so it is compulsory) |
| 167 | D164 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 168 | D165 | Design Number blank while TDW = 2.96 (>0, so it is compulsory) |
| 169 | D166 | Design Number blank while TDW = 2.97 (>0, so it is compulsory) |
| 170 | D167 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 171 | D168 | Design Number blank while TDW = 10.12 (>0, so it is compulsory) |
| 172 | D169 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 173 | D170 | Design Number blank while TDW = 10.08 (>0, so it is compulsory) |
| 174 | D171 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 175 | D172 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 176 | D173 | Design Number blank while TDW = 10.08 (>0, so it is compulsory) |
| 177 | D174 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 178 | D175 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 179 | D176 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 180 | D177 | Design Number blank while TDW = 10.13 (>0, so it is compulsory) |
| 181 | D178 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 182 | D179 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 183 | D180 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 184 | D181 | Design Number blank while TDW = 10.15 (>0, so it is compulsory) |
| 185 | D182 | Design Number blank while TDW = 10.74 (>0, so it is compulsory) |
| 186 | D183 | Design Number blank while TDW = 10.11 (>0, so it is compulsory) |
| 187 | D184 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 188 | D185 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 189 | D186 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 190 | D187 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 191 | D188 | Design Number blank while TDW = 10.02 (>0, so it is compulsory) |
| 192 | D189 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 193 | D190 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| 194 | D191 | Design Number blank while TDW = 5.17 (>0, so it is compulsory) |
| 195 | D192 | Design Number blank while TDW = 5.16 (>0, so it is compulsory) |
| 196 | D193 | Design Number blank while TDW = 5.17 (>0, so it is compulsory) |
| 197 | D194 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 198 | D195 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 199 | D196 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 200 | D197 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 201 | D198 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 202 | D199 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 203 | D200 | Design Number blank while TDW = 5.29 (>0, so it is compulsory) |
| 204 | D201 | Design Number blank while TDW = 5.26 (>0, so it is compulsory) |
| 205 | D202 | Design Number blank while TDW = 5.17 (>0, so it is compulsory) |
| 206 | D203 | Design Number blank while TDW = 5.17 (>0, so it is compulsory) |
| 207 | D204 | Design Number blank while TDW = 5.22 (>0, so it is compulsory) |
| 208 | D205 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 209 | D206 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 210 | D207 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 211 | D208 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 212 | D209 | Design Number blank while TDW = 5.22 (>0, so it is compulsory) |
| 213 | D210 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 214 | D211 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 215 | D212 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 216 | D213 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 217 | D214 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 218 | D215 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 219 | D216 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 220 | D217 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 221 | D218 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 222 | D219 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 223 | D220 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 224 | D221 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 225 | D222 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 226 | D223 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 227 | D224 | Design Number blank while TDW = 5.27 (>0, so it is compulsory) |
| 228 | D225 | Design Number blank while TDW = 5.22 (>0, so it is compulsory) |
| 229 | D226 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 230 | D227 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 231 | D228 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 232 | D229 | Design Number blank while TDW = 5.25 (>0, so it is compulsory) |
| 233 | D230 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 234 | D231 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 235 | D232 | Design Number blank while TDW = 5.23 (>0, so it is compulsory) |
| 236 | D233 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 237 | D234 | Design Number blank while TDW = 3.46 (>0, so it is compulsory) |
| 238 | D235 | Design Number blank while TDW = 4.13 (>0, so it is compulsory) |
| 239 | D236 | Design Number blank while TDW = 4.13 (>0, so it is compulsory) |
| 240 | D237 | Design Number blank while TDW = 3.45 (>0, so it is compulsory) |
| 241 | D238 | Design Number blank while TDW = 2.62 (>0, so it is compulsory) |
| 242 | D239 | Design Number blank while TDW = 3.42 (>0, so it is compulsory) |
| 243 | D240 | Design Number blank while TDW = 3.49 (>0, so it is compulsory) |
| 244 | D241 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 245 | D242 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 246 | D243 | Design Number blank while TDW = 1.96 (>0, so it is compulsory) |
| 247 | D244 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 248 | D245 | Design Number blank while TDW = 2.53 (>0, so it is compulsory) |
| 249 | D246 | Design Number blank while TDW = 2.19 (>0, so it is compulsory) |
| 250 | D247 | Design Number blank while TDW = 1.52 (>0, so it is compulsory) |
| 251 | D248 | Design Number blank while TDW = 1.51 (>0, so it is compulsory) |
| 252 | D249 | Design Number blank while TDW = 1.53 (>0, so it is compulsory) |
| 253 | D250 | Design Number blank while TDW = 1.53 (>0, so it is compulsory) |
| 254 | D251 | Design Number blank while TDW = 2.0 (>0, so it is compulsory) |
| 255 | D252 | Design Number blank while TDW = 1.8 (>0, so it is compulsory) |
| 256 | D253 | Design Number blank while TDW = 2.0 (>0, so it is compulsory) |
| 257 | D254 | Design Number blank while TDW = 1.81 (>0, so it is compulsory) |
| 258 | D255 | Design Number blank while TDW = 2.6 (>0, so it is compulsory) |
| 259 | D256 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 260 | D257 | Design Number blank while TDW = 1.92 (>0, so it is compulsory) |
| 261 | D258 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 262 | D259 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 263 | D260 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 264 | D261 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 265 | D262 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 266 | D263 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 267 | D264 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 268 | D265 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 269 | D266 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 270 | D267 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 271 | D268 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 272 | D269 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 273 | D270 | Design Number blank while TDW = 10.07 (>0, so it is compulsory) |
| 274 | D271 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 275 | D272 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 276 | D273 | Design Number blank while TDW = 10.08 (>0, so it is compulsory) |
| 277 | D274 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 278 | D275 | Design Number blank while TDW = 10.13 (>0, so it is compulsory) |
| 279 | D276 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 280 | D277 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 281 | D278 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 282 | D279 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 283 | D280 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 284 | D281 | Design Number blank while TDW = 7.09 (>0, so it is compulsory) |
| 285 | D282 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 286 | D283 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 287 | D284 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 288 | D285 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 289 | D286 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 290 | D287 | Design Number blank while TDW = 5.13 (>0, so it is compulsory) |
| 291 | D288 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 292 | D289 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 293 | D290 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 294 | D291 | Design Number blank while TDW = 7.06 (>0, so it is compulsory) |
| 295 | D292 | Design Number blank while TDW = 7.06 (>0, so it is compulsory) |
| 296 | D293 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 297 | D294 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 298 | D295 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 299 | D296 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 300 | D297 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 301 | D298 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 302 | D299 | Design Number blank while TDW = 7.24 (>0, so it is compulsory) |
| 303 | D300 | Design Number blank while TDW = 10.07 (>0, so it is compulsory) |
| 304 | D301 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 305 | D302 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 306 | D303 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 307 | D304 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 308 | D305 | Design Number blank while TDW = 10.08 (>0, so it is compulsory) |
| 309 | D306 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 310 | D307 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 311 | D308 | Design Number blank while TDW = 10.13 (>0, so it is compulsory) |
| 312 | D309 | Design Number blank while TDW = 10.06 (>0, so it is compulsory) |
| 313 | D310 | Design Number blank while TDW = 10.02 (>0, so it is compulsory) |
| 314 | D311 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 315 | D312 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 316 | D313 | Design Number blank while TDW = 5.11 (>0, so it is compulsory) |
| 317 | D314 | Design Number blank while TDW = 5.12 (>0, so it is compulsory) |
| 318 | D315 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 319 | D316 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 320 | D317 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 321 | D318 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 322 | D319 | Design Number blank while TDW = 5.14 (>0, so it is compulsory) |
| 323 | D320 | Design Number blank while TDW = 10.04 (>0, so it is compulsory) |
| 324 | D321 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 325 | D322 | Design Number blank while TDW = 7.07 (>0, so it is compulsory) |
| 326 | D323 | Design Number blank while TDW = 7.09 (>0, so it is compulsory) |
| 327 | D324 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 328 | D325 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 329 | D326 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 330 | D327 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 331 | D328 | Design Number blank while TDW = 6.93 (>0, so it is compulsory) |
| 332 | D329 | Design Number blank while TDW = 6.96 (>0, so it is compulsory) |
| 333 | D330 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 334 | D331 | Design Number blank while TDW = 21.66 (>0, so it is compulsory) |
| 334 | R331 | Product Code '0.0' is not on the Price List |
| 335 | D332 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 336 | D333 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 337 | D334 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 338 | D335 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 339 | D336 | Design Number blank while TDW = 6.94 (>0, so it is compulsory) |
| 340 | D337 | Design Number blank while TDW = 6.91 (>0, so it is compulsory) |
| 341 | D338 | Design Number blank while TDW = 6.98 (>0, so it is compulsory) |
| 342 | D339 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| 343 | D340 | Design Number blank while TDW = 5.21 (>0, so it is compulsory) |
| 344 | D341 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 345 | D342 | Design Number blank while TDW = 5.13 (>0, so it is compulsory) |
| 346 | D343 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 347 | D344 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 348 | D345 | Design Number blank while TDW = 5.14 (>0, so it is compulsory) |
| 349 | D346 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 350 | D347 | Design Number blank while TDW = 5.17 (>0, so it is compulsory) |
| 351 | D348 | Design Number blank while TDW = 6.92 (>0, so it is compulsory) |
| 352 | D349 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 353 | D350 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 354 | D351 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 355 | D352 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 356 | D353 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 357 | D354 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 358 | D355 | Design Number blank while TDW = 10.68 (>0, so it is compulsory) |
| 359 | D356 | Design Number blank while TDW = 5.13 (>0, so it is compulsory) |
| 360 | D357 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 361 | D358 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 362 | D359 | Design Number blank while TDW = 27.48 (>0, so it is compulsory) |
| 363 | D360 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 364 | D361 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 365 | D362 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 366 | D363 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 367 | D364 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 368 | D365 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 369 | D366 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 370 | D367 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 371 | D368 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 372 | D369 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 373 | D370 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 374 | D371 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 375 | D372 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 376 | D373 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 377 | D374 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 378 | D375 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 379 | D376 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 380 | D377 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 381 | D378 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 382 | D379 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 383 | D380 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 384 | D381 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 385 | D382 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 386 | D383 | Design Number blank while TDW = 12.09 (>0, so it is compulsory) |
| 387 | D384 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 387 | G384 | Ring size 'US 7' has a space — expected 'US7' |
| 388 | D385 | Design Number blank while TDW = 3.26 (>0, so it is compulsory) |
| 388 | G385 | Ring size 'US 7' has a space — expected 'US7' |
| 389 | D386 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 390 | D387 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 391 | D388 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 392 | D389 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 393 | D390 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 394 | D391 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 395 | D392 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 396 | D393 | Design Number blank while TDW = 5.12 (>0, so it is compulsory) |
| 397 | D394 | Design Number blank while TDW = 5.12 (>0, so it is compulsory) |
| 398 | D395 | Design Number blank while TDW = 5.12 (>0, so it is compulsory) |
| 399 | D396 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 400 | D397 | Design Number blank while TDW = 5.11 (>0, so it is compulsory) |
| 401 | D398 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 402 | D399 | Design Number blank while TDW = 5.12 (>0, so it is compulsory) |
| 403 | D400 | Design Number blank while TDW = 10.52 (>0, so it is compulsory) |
| 404 | D401 | Design Number blank while TDW = 10.44 (>0, so it is compulsory) |
| 405 | D402 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 406 | D403 | Design Number blank while TDW = 7.06 (>0, so it is compulsory) |
| 407 | D404 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 408 | D405 | Design Number blank while TDW = 7.11 (>0, so it is compulsory) |
| 409 | D406 | Design Number blank while TDW = 7.04 (>0, so it is compulsory) |
| 410 | D407 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 411 | D408 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 412 | D409 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 413 | D410 | Design Number blank while TDW = 7.11 (>0, so it is compulsory) |
| 414 | D411 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 415 | D412 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 416 | D413 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 417 | D414 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 418 | D415 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 419 | D416 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 420 | D417 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 421 | D418 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 422 | D419 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 423 | D420 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 424 | D421 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 425 | D422 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 426 | D423 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 427 | D424 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 428 | D425 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 429 | D426 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 430 | D427 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 431 | D428 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 432 | D429 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 433 | D430 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 434 | D431 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 435 | D432 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 436 | D433 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 437 | D434 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 438 | D435 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 439 | D436 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 440 | D437 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 441 | D438 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 442 | D439 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 443 | D440 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 444 | D441 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 445 | D442 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 446 | D443 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 447 | D444 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 448 | D445 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 449 | D446 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 450 | D447 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 451 | D448 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 452 | D449 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 453 | D450 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 454 | D451 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 455 | D452 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 456 | D453 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 457 | D454 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 458 | D455 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 459 | D456 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 460 | D457 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 461 | D458 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 462 | D459 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 463 | D460 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 464 | D461 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 465 | D462 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 466 | D463 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 467 | D464 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 468 | D465 | Design Number blank while TDW = 0.94 (>0, so it is compulsory) |
| 468 | G465 | Ring size 'US 7' has a space — expected 'US7' |
| 469 | D466 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 470 | D467 | Design Number blank while TDW = 9.96 (>0, so it is compulsory) |
| 471 | D468 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 472 | D469 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 473 | D470 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 474 | D471 | Design Number blank while TDW = 3.56 (>0, so it is compulsory) |
| 474 | G471 | Ring size 'US 7' has a space — expected 'US7' |
| 475 | D472 | Design Number blank while TDW = 2.42 (>0, so it is compulsory) |
| 475 | G472 | Ring size 'US 7' has a space — expected 'US7' |
| 476 | D473 | Design Number blank while TDW = 1.5 (>0, so it is compulsory) |
| 477 | D474 | Design Number blank while TDW = 5.13 (>0, so it is compulsory) |
| 478 | D475 | Design Number blank while TDW = 1.39 (>0, so it is compulsory) |
| 479 | D476 | Design Number blank while TDW = 0.98 (>0, so it is compulsory) |
| 480 | D477 | Design Number blank while TDW = 1.88 (>0, so it is compulsory) |
| 481 | D478 | Design Number blank while TDW = 22.04 (>0, so it is compulsory) |
| 482 | D479 | Design Number blank while TDW = 7.27 (>0, so it is compulsory) |
| 483 | D480 | Design Number blank while TDW = 7.26 (>0, so it is compulsory) |
| 484 | D481 | Design Number blank while TDW = 7.28 (>0, so it is compulsory) |
| 485 | D482 | Design Number blank while TDW = 7.26 (>0, so it is compulsory) |
| 486 | D483 | Design Number blank while TDW = 10.37 (>0, so it is compulsory) |
| 487 | D484 | Design Number blank while TDW = 10.3 (>0, so it is compulsory) |
| 488 | D485 | Design Number blank while TDW = 10.37 (>0, so it is compulsory) |
| 489 | D486 | Design Number blank while TDW = 10.39 (>0, so it is compulsory) |
| 490 | D487 | Design Number blank while TDW = 2.42 (>0, so it is compulsory) |
| 490 | G487 | Ring size 'US 7' has a space — expected 'US7' |
| 491 | D488 | Design Number blank while TDW = 2.22 (>0, so it is compulsory) |
| 491 | G488 | Ring size 'US 7' has a space — expected 'US7' |
| 492 | D489 | Design Number blank while TDW = 2.05 (>0, so it is compulsory) |
| 493 | D490 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 494 | D491 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 495 | D492 | Design Number blank while TDW = 2.0 (>0, so it is compulsory) |
| 496 | D493 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 497 | D494 | Design Number blank while TDW = 2.14 (>0, so it is compulsory) |
| 498 | D495 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 499 | D496 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 500 | D497 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 501 | D498 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 502 | D499 | Design Number blank while TDW = 10.5 (>0, so it is compulsory) |
| 503 | D500 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 504 | D501 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 505 | D502 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 506 | D503 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 507 | D504 | Design Number blank while TDW = 10.02 (>0, so it is compulsory) |
| 508 | D505 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 509 | D506 | Design Number blank while TDW = 15.29 (>0, so it is compulsory) |
| 510 | D507 | Design Number blank while TDW = 15.31 (>0, so it is compulsory) |
| 511 | D508 | Design Number blank while TDW = 10.26 (>0, so it is compulsory) |
| 512 | D509 | Design Number blank while TDW = 5.36 (>0, so it is compulsory) |
| 512 | G509 | Ring size 'US 7' has a space — expected 'US7' |
| 513 | D510 | Design Number blank while TDW = 5.35 (>0, so it is compulsory) |
| 513 | G510 | Ring size 'US 7' has a space — expected 'US7' |
| 514 | D511 | Design Number blank while TDW = 5.36 (>0, so it is compulsory) |
| 514 | G511 | Ring size 'US 7' has a space — expected 'US7' |
| 515 | D512 | Design Number blank while TDW = 5.36 (>0, so it is compulsory) |
| 515 | G512 | Ring size 'US 7' has a space — expected 'US7' |
| 516 | D513 | Design Number blank while TDW = 5.36 (>0, so it is compulsory) |
| 516 | G513 | Ring size 'US 7' has a space — expected 'US7' |
| 517 | D514 | Design Number blank while TDW = 5.35 (>0, so it is compulsory) |
| 517 | G514 | Ring size 'US 7' has a space — expected 'US7' |
| 518 | D515 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 519 | D516 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 520 | D517 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 521 | D518 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 522 | D519 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 523 | D520 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 524 | D521 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 525 | D522 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 526 | D523 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 527 | I524 | TDW = 0 but net 11.505 != gross 12.915. With no diamonds they should be equal |
| 528 | D525 | Design Number blank while TDW = 37.34 (>0, so it is compulsory) |
| 529 | D526 | Design Number blank while TDW = 5.13 (>0, so it is compulsory) |
| 530 | D527 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 531 | D528 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 532 | D529 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 533 | D530 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 534 | D531 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 535 | D532 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 536 | D533 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 537 | D534 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 538 | D535 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 539 | D536 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 540 | D537 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 541 | D538 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 542 | D539 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 543 | D540 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 544 | D541 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 545 | D542 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 546 | D543 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 547 | D544 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 548 | D545 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 549 | D546 | Design Number blank while TDW = 2.96 (>0, so it is compulsory) |
| 550 | D547 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 551 | D548 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 552 | D549 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 553 | D550 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 554 | D551 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 555 | D552 | Design Number blank while TDW = 2.96 (>0, so it is compulsory) |
| 556 | D553 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 557 | D554 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 558 | D555 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 559 | D556 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 560 | D557 | Design Number blank while TDW = 2.99 (>0, so it is compulsory) |
| 561 | D558 | Design Number blank while TDW = 2.96 (>0, so it is compulsory) |
| 562 | D559 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 563 | D560 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 564 | D561 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 565 | D562 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 566 | D563 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 567 | D564 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 568 | D565 | Design Number blank while TDW = 6.99 (>0, so it is compulsory) |
| 569 | D566 | Design Number blank while TDW = 6.96 (>0, so it is compulsory) |
| 570 | D567 | Design Number blank while TDW = 6.92 (>0, so it is compulsory) |
| 571 | D568 | Design Number blank while TDW = 6.95 (>0, so it is compulsory) |
| 572 | D569 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 573 | D570 | Design Number blank while TDW = 6.96 (>0, so it is compulsory) |
| 574 | D571 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 575 | D572 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 576 | D573 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 577 | D574 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 578 | D575 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 579 | D576 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 580 | D577 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 581 | D578 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 582 | D579 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 583 | D580 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 584 | D581 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 585 | D582 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 586 | D583 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 587 | D584 | Design Number blank while TDW = 5.06 (>0, so it is compulsory) |
| 588 | D585 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 589 | D586 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 590 | D587 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 591 | D588 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 592 | D589 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 593 | D590 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 594 | D591 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 595 | D592 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 596 | D593 | Design Number blank while TDW = 5.07 (>0, so it is compulsory) |
| 597 | D594 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 598 | D595 | Design Number blank while TDW = 7.25 (>0, so it is compulsory) |
| 599 | D596 | Design Number blank while TDW = 15.47 (>0, so it is compulsory) |
| 600 | D597 | Design Number blank while TDW = 15.32 (>0, so it is compulsory) |
| 601 | D598 | Design Number blank while TDW = 15.41 (>0, so it is compulsory) |
| 602 | D599 | Design Number blank while TDW = 3.29 (>0, so it is compulsory) |
| 602 | G599 | Ring size 'US 7' has a space — expected 'US7' |
| 603 | D600 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 603 | G600 | Ring size 'US 7' has a space — expected 'US7' |
| 604 | D601 | Design Number blank while TDW = 3.7 (>0, so it is compulsory) |
| 605 | D602 | Design Number blank while TDW = 2.08 (>0, so it is compulsory) |
| 606 | D603 | Design Number blank while TDW = 1.61 (>0, so it is compulsory) |
| 606 | G603 | Ring size 'US 7' has a space — expected 'US7' |
| 607 | D604 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 608 | D605 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 609 | D606 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 610 | D607 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 611 | D608 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 612 | D609 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 613 | D610 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 614 | D611 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 615 | D612 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 616 | D613 | Design Number blank while TDW = 5.09 (>0, so it is compulsory) |
| 617 | D614 | Design Number blank while TDW = 5.09 (>0, so it is compulsory) |
| 618 | D615 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 619 | D616 | Design Number blank while TDW = 5.09 (>0, so it is compulsory) |
| 620 | D617 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 621 | D618 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 622 | D619 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 623 | D620 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 624 | D621 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 625 | D622 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 626 | D623 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 627 | D624 | Design Number blank while TDW = 5.09 (>0, so it is compulsory) |
| 628 | D625 | Design Number blank while TDW = 5.09 (>0, so it is compulsory) |
| 629 | D626 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 630 | D627 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 631 | D628 | Design Number blank while TDW = 8.15 (>0, so it is compulsory) |
| 632 | D629 | Design Number blank while TDW = 4.05 (>0, so it is compulsory) |
| 633 | D630 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 634 | D631 | Design Number blank while TDW = 4.05 (>0, so it is compulsory) |
| 635 | D632 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 636 | D633 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 637 | D634 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 638 | D635 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 639 | D636 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 640 | D637 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 641 | D638 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 642 | D639 | Design Number blank while TDW = 4.05 (>0, so it is compulsory) |
| 643 | D640 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 644 | D641 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 645 | D642 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 646 | D643 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 647 | D644 | Design Number blank while TDW = 25.41 (>0, so it is compulsory) |
| 648 | D645 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 649 | D646 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 650 | D647 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 651 | D648 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 652 | D649 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 653 | D650 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 654 | D651 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 655 | D652 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 656 | D653 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 657 | D654 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 658 | D655 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 659 | D656 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 660 | D657 | Design Number blank while TDW = 3.02 (>0, so it is compulsory) |
| 661 | D658 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 662 | D659 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 663 | D660 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 664 | D661 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 665 | D662 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 666 | D663 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 667 | D664 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 668 | D665 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 669 | D666 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 670 | D667 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 671 | D668 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 672 | D669 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 673 | D670 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 674 | D671 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 675 | D672 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 676 | D673 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 677 | D674 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 678 | D675 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 679 | D676 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 680 | D677 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 681 | D678 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 682 | D679 | Design Number blank while TDW = 7.33 (>0, so it is compulsory) |
| 683 | D680 | Design Number blank while TDW = 20.12 (>0, so it is compulsory) |
| 684 | D681 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 685 | D682 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 686 | D683 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 687 | D684 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 688 | D685 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 689 | D686 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 690 | D687 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 691 | D688 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 692 | D689 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 693 | D690 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 694 | D691 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 695 | D692 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 696 | D693 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 697 | D694 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 698 | D695 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 699 | D696 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 700 | D697 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 701 | D698 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 702 | D699 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 703 | D700 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 704 | D701 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 705 | D702 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 706 | D703 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 707 | D704 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 708 | D705 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 709 | D706 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 710 | D707 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 711 | D708 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 712 | D709 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 713 | D710 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 714 | D711 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 715 | D712 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 716 | D713 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 717 | D714 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 718 | D715 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 719 | D716 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 720 | D717 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 721 | D718 | Design Number blank while TDW = 65.325 (>0, so it is compulsory) |
| 722 | D719 | Design Number blank while TDW = 65.99 (>0, so it is compulsory) |
| 722 | K719 | Single row: breakup 80.98 != TDW 65.99 |
| 723 | D720 | Design Number blank while TDW = 15.985 (>0, so it is compulsory) |
| 724 | D721 | Design Number blank while TDW = 80.35 (>0, so it is compulsory) |
| 725 | D722 | Design Number blank while TDW = 22.76 (>0, so it is compulsory) |
| 726 | D723 | Design Number blank while TDW = 2.03 (>0, so it is compulsory) |
| 727 | D724 | Design Number blank while TDW = 2.13 (>0, so it is compulsory) |
| 728 | D725 | Design Number blank while TDW = 2.19 (>0, so it is compulsory) |
| 729 | D726 | Design Number blank while TDW = 4.09 (>0, so it is compulsory) |
| 730 | D727 | Design Number blank while TDW = 2.05 (>0, so it is compulsory) |
| 731 | D728 | Design Number blank while TDW = 2.4 (>0, so it is compulsory) |
| 732 | D729 | Design Number blank while TDW = 2.6 (>0, so it is compulsory) |
| 733 | D730 | Design Number blank while TDW = 2.18 (>0, so it is compulsory) |
| 734 | D731 | Design Number blank while TDW = 2.98 (>0, so it is compulsory) |
| 735 | D732 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 736 | D733 | Design Number blank while TDW = 2.3 (>0, so it is compulsory) |
| 737 | D734 | Design Number blank while TDW = 2.07 (>0, so it is compulsory) |
| 738 | D735 | Design Number blank while TDW = 2.06 (>0, so it is compulsory) |
| 739 | D736 | Design Number blank while TDW = 1.94 (>0, so it is compulsory) |
| 740 | D737 | Design Number blank while TDW = 4.18 (>0, so it is compulsory) |
| 741 | D738 | Design Number blank while TDW = 2.22 (>0, so it is compulsory) |
| 742 | D739 | Design Number blank while TDW = 2.09 (>0, so it is compulsory) |
| 743 | D740 | Design Number blank while TDW = 2.11 (>0, so it is compulsory) |
| 744 | D741 | Design Number blank while TDW = 2.21 (>0, so it is compulsory) |
| 745 | D742 | Design Number blank while TDW = 2.42 (>0, so it is compulsory) |
| 746 | D743 | Design Number blank while TDW = 2.14 (>0, so it is compulsory) |
| 747 | D744 | Design Number blank while TDW = 5.12 (>0, so it is compulsory) |
| 748 | D745 | Design Number blank while TDW = 2.2 (>0, so it is compulsory) |
| 749 | D746 | Design Number blank while TDW = 2.44 (>0, so it is compulsory) |
| 750 | D747 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 751 | D748 | Design Number blank while TDW = 5.11 (>0, so it is compulsory) |
| 752 | D749 | Design Number blank while TDW = 2.11 (>0, so it is compulsory) |
| 753 | D750 | Design Number blank while TDW = 1.93 (>0, so it is compulsory) |
| 754 | D751 | Design Number blank while TDW = 1.94 (>0, so it is compulsory) |
| 755 | D752 | Design Number blank while TDW = 2.55 (>0, so it is compulsory) |
| 756 | D753 | Design Number blank while TDW = 4.13 (>0, so it is compulsory) |
| 757 | D754 | Design Number blank while TDW = 2.06 (>0, so it is compulsory) |
| 758 | D755 | Design Number blank while TDW = 2.71 (>0, so it is compulsory) |
| 759 | D756 | Design Number blank while TDW = 2.12 (>0, so it is compulsory) |
| 760 | D757 | Design Number blank while TDW = 2.07 (>0, so it is compulsory) |
| 761 | D758 | Design Number blank while TDW = 2.17 (>0, so it is compulsory) |
| 762 | D759 | Design Number blank while TDW = 2.04 (>0, so it is compulsory) |
| 763 | D760 | Design Number blank while TDW = 2.76 (>0, so it is compulsory) |
| 764 | D761 | Design Number blank while TDW = 2.16 (>0, so it is compulsory) |
| 765 | D762 | Design Number blank while TDW = 2.03 (>0, so it is compulsory) |
| 766 | D763 | Design Number blank while TDW = 2.13 (>0, so it is compulsory) |
| 767 | D764 | Design Number blank while TDW = 2.53 (>0, so it is compulsory) |
| 768 | D765 | Design Number blank while TDW = 2.53 (>0, so it is compulsory) |
| 769 | D766 | Design Number blank while TDW = 2.22 (>0, so it is compulsory) |
| 769 | G766 | Ring size 'US 7' has a space — expected 'US7' |
| 770 | D767 | Design Number blank while TDW = 1.23 (>0, so it is compulsory) |
| 770 | G767 | Ring size 'US 7' has a space — expected 'US7' |
| 771 | D768 | Design Number blank while TDW = 1.44 (>0, so it is compulsory) |
| 771 | G768 | Ring size 'US 7' has a space — expected 'US7' |
| 772 | D769 | Design Number blank while TDW = 1.13 (>0, so it is compulsory) |
| 772 | G769 | Ring size 'US 7' has a space — expected 'US7' |
| 773 | D770 | Design Number blank while TDW = 1.94 (>0, so it is compulsory) |
| 773 | G770 | Ring size 'US 7' has a space — expected 'US7' |
| 774 | D771 | Design Number blank while TDW = 1.45 (>0, so it is compulsory) |
| 774 | G771 | Ring size 'US 7' has a space — expected 'US7' |
| 775 | D772 | Design Number blank while TDW = 1.15 (>0, so it is compulsory) |
| 775 | G772 | Ring size 'US 7' has a space — expected 'US7' |
| 776 | D773 | Design Number blank while TDW = 3.38 (>0, so it is compulsory) |
| 776 | G773 | Ring size 'US 7' has a space — expected 'US7' |
| 777 | D774 | Design Number blank while TDW = 1.18 (>0, so it is compulsory) |
| 777 | G774 | Ring size 'US 7' has a space — expected 'US7' |
| 778 | D775 | Design Number blank while TDW = 1.24 (>0, so it is compulsory) |
| 778 | G775 | Ring size 'US 7' has a space — expected 'US7' |
| 779 | D776 | Design Number blank while TDW = 1.54 (>0, so it is compulsory) |
| 779 | G776 | Ring size 'US 7' has a space — expected 'US7' |
| 780 | D777 | Design Number blank while TDW = 1.37 (>0, so it is compulsory) |
| 780 | G777 | Ring size 'US 7' has a space — expected 'US7' |
| 781 | D778 | Design Number blank while TDW = 1.55 (>0, so it is compulsory) |
| 781 | G778 | Ring size 'US 7' has a space — expected 'US7' |
| 782 | D779 | Design Number blank while TDW = 1.12 (>0, so it is compulsory) |
| 782 | G779 | Ring size 'US 7' has a space — expected 'US7' |
| 783 | D780 | Design Number blank while TDW = 1.17 (>0, so it is compulsory) |
| 783 | G780 | Ring size 'US 7' has a space — expected 'US7' |
| 784 | D781 | Design Number blank while TDW = 1.15 (>0, so it is compulsory) |
| 784 | G781 | Ring size 'US 7' has a space — expected 'US7' |
| 785 | D782 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 786 | D783 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 787 | D784 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 788 | D785 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 789 | D786 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 790 | D787 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 791 | D788 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 792 | D789 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 793 | D790 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 794 | D791 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 795 | D792 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 796 | D793 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 797 | D794 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 798 | D795 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 799 | D796 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 800 | D797 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 801 | D798 | Design Number blank while TDW = 1.01 (>0, so it is compulsory) |
| 801 | G798 | Ring size 'US 7' has a space — expected 'US7' |
| 802 | D799 | Design Number blank while TDW = 4.59 (>0, so it is compulsory) |
| 802 | G799 | Ring size 'US 7' has a space — expected 'US7' |
| 803 | D800 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 803 | G800 | Ring size 'US 7' has a space — expected 'US7' |
| 804 | D801 | Design Number blank while TDW = 1.03 (>0, so it is compulsory) |
| 804 | G801 | Ring size 'US 7' has a space — expected 'US7' |
| 805 | D802 | Design Number blank while TDW = 2.22 (>0, so it is compulsory) |
| 805 | G802 | Ring size 'US 7' has a space — expected 'US7' |
| 806 | D803 | Design Number blank while TDW = 1.14 (>0, so it is compulsory) |
| 806 | G803 | Ring size 'US 7' has a space — expected 'US7' |
| 807 | D804 | Design Number blank while TDW = 1.83 (>0, so it is compulsory) |
| 807 | G804 | Ring size 'US 7' has a space — expected 'US7' |
| 808 | D805 | Design Number blank while TDW = 1.44 (>0, so it is compulsory) |
| 808 | G805 | Ring size 'US 7' has a space — expected 'US7' |
| 809 | D806 | Design Number blank while TDW = 1.28 (>0, so it is compulsory) |
| 809 | G806 | Ring size 'US 7' has a space — expected 'US7' |
| 810 | D807 | Design Number blank while TDW = 1.48 (>0, so it is compulsory) |
| 810 | G807 | Ring size 'US 7' has a space — expected 'US7' |
| 811 | D808 | Design Number blank while TDW = 2.92 (>0, so it is compulsory) |
| 811 | G808 | Ring size 'US 7' has a space — expected 'US7' |
| 812 | D809 | Design Number blank while TDW = 1.01 (>0, so it is compulsory) |
| 812 | G809 | Ring size 'US 7' has a space — expected 'US7' |
| 813 | D810 | Design Number blank while TDW = 1.01 (>0, so it is compulsory) |
| 813 | G810 | Ring size 'US 7' has a space — expected 'US7' |
| 814 | D811 | Design Number blank while TDW = 1.47 (>0, so it is compulsory) |
| 814 | G811 | Ring size 'US 7' has a space — expected 'US7' |
| 815 | D812 | Design Number blank while TDW = 0.92 (>0, so it is compulsory) |
| 815 | G812 | Ring size 'US 7' has a space — expected 'US7' |
| 816 | D813 | Design Number blank while TDW = 1.19 (>0, so it is compulsory) |
| 816 | G813 | Ring size 'US 7' has a space — expected 'US7' |
| 817 | D814 | Design Number blank while TDW = 1.96 (>0, so it is compulsory) |
| 817 | G814 | Ring size 'US 7' has a space — expected 'US7' |
| 818 | D815 | Design Number blank while TDW = 1.8 (>0, so it is compulsory) |
| 818 | G815 | Ring size 'US 7' has a space — expected 'US7' |
| 819 | D816 | Design Number blank while TDW = 4.55 (>0, so it is compulsory) |
| 819 | G816 | Ring size 'US 7' has a space — expected 'US7' |
| 820 | D817 | Design Number blank while TDW = 2.88 (>0, so it is compulsory) |
| 820 | G817 | Ring size 'US 7' has a space — expected 'US7' |
| 821 | D818 | Design Number blank while TDW = 21.93 (>0, so it is compulsory) |
| 822 | D819 | Design Number blank while TDW = 24.05 (>0, so it is compulsory) |
| 823 | D820 | Design Number blank while TDW = 12.25 (>0, so it is compulsory) |
| 824 | D821 | Design Number blank while TDW = 2.33 (>0, so it is compulsory) |
| 825 | D822 | Design Number blank while TDW = 1.52 (>0, so it is compulsory) |
| 825 | G822 | Ring size 'US 7' has a space — expected 'US7' |
| 826 | D823 | Design Number blank while TDW = 2.87 (>0, so it is compulsory) |
| 827 | D824 | Design Number blank while TDW = 32.87 (>0, so it is compulsory) |
| 828 | D825 | Design Number blank while TDW = 2.135 (>0, so it is compulsory) |
| 829 | D826 | Design Number blank while TDW = 1.98 (>0, so it is compulsory) |
| 829 | G826 | Ring size 'US 7' has a space — expected 'US7' |
| 830 | D827 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 830 | G827 | Ring size 'US 7' has a space — expected 'US7' |
| 831 | D828 | Design Number blank while TDW = 0.94 (>0, so it is compulsory) |
| 831 | G828 | Ring size 'US 7' has a space — expected 'US7' |
| 832 | D829 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 832 | G829 | Ring size 'US 7' has a space — expected 'US7' |
| 833 | D830 | Design Number blank while TDW = 1.46 (>0, so it is compulsory) |
| 833 | G830 | Ring size 'US 7' has a space — expected 'US7' |
| 834 | D831 | Design Number blank while TDW = 21.06 (>0, so it is compulsory) |
| 835 | D832 | Design Number blank while TDW = 1.16 (>0, so it is compulsory) |
| 835 | G832 | Ring size 'US 7' has a space — expected 'US7' |
| 836 | D833 | Design Number blank while TDW = 8.11 (>0, so it is compulsory) |
| 837 | D834 | Design Number blank while TDW = 7.07 (>0, so it is compulsory) |
| 838 | D835 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 838 | G835 | Ring size 'US 7' has a space — expected 'US7' |
| 839 | D836 | Design Number blank while TDW = 2.64 (>0, so it is compulsory) |
| 840 | D837 | Design Number blank while TDW = 2.425 (>0, so it is compulsory) |
| 841 | D838 | Design Number blank while TDW = 2.755 (>0, so it is compulsory) |
| 842 | D839 | Design Number blank while TDW = 2.19 (>0, so it is compulsory) |
| 843 | D840 | Design Number blank while TDW = 2.605 (>0, so it is compulsory) |
| 844 | D841 | Design Number blank while TDW = 2.04 (>0, so it is compulsory) |
| 845 | D842 | Design Number blank while TDW = 2.44 (>0, so it is compulsory) |
| 846 | D843 | Design Number blank while TDW = 1.5 (>0, so it is compulsory) |
| 846 | G843 | Ring size 'US 7' has a space — expected 'US7' |
| 847 | D844 | Design Number blank while TDW = 2.165 (>0, so it is compulsory) |
| 848 | D845 | Design Number blank while TDW = 2.1 (>0, so it is compulsory) |
| 849 | H846 | GROSS WEIGHT is zero |
| 850 | D847 | Design Number blank while TDW = 2.9 (>0, so it is compulsory) |
| 851 | D848 | Design Number blank while TDW = 2.19 (>0, so it is compulsory) |
| 852 | D849 | Design Number blank while TDW = 2.19 (>0, so it is compulsory) |
| 853 | D850 | Design Number blank while TDW = 16.165 (>0, so it is compulsory) |
| 854 | D851 | Design Number blank while TDW = 22.09 (>0, so it is compulsory) |
| 855 | D852 | Design Number blank while TDW = 9.49 (>0, so it is compulsory) |
| 856 | D853 | Design Number blank while TDW = 2.84 (>0, so it is compulsory) |
| 856 | G853 | Ring size 'US 7' has a space — expected 'US7' |
| 857 | D854 | Design Number blank while TDW = 2.1 (>0, so it is compulsory) |
| 857 | G854 | Ring size 'US 7' has a space — expected 'US7' |
| 858 | D855 | Design Number blank while TDW = 2.85 (>0, so it is compulsory) |
| 858 | G855 | Ring size 'US 7' has a space — expected 'US7' |
| 859 | D856 | Design Number blank while TDW = 4.45 (>0, so it is compulsory) |
| 859 | G856 | Ring size 'US 7' has a space — expected 'US7' |
| 860 | D857 | Design Number blank while TDW = 1.93 (>0, so it is compulsory) |
| 860 | G857 | Ring size 'US 7' has a space — expected 'US7' |
| 861 | D858 | Design Number blank while TDW = 1.94 (>0, so it is compulsory) |
| 861 | G858 | Ring size 'US 7' has a space — expected 'US7' |
| 862 | D859 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 862 | G859 | Ring size 'US 7' has a space — expected 'US7' |
| 863 | D860 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 863 | G860 | Ring size 'US 7' has a space — expected 'US7' |
| 864 | D861 | Design Number blank while TDW = 4.48 (>0, so it is compulsory) |
| 864 | G861 | Ring size 'US 7' has a space — expected 'US7' |
| 865 | D862 | Design Number blank while TDW = 2.09 (>0, so it is compulsory) |
| 865 | G862 | Ring size 'US 7' has a space — expected 'US7' |
| 866 | D863 | Design Number blank while TDW = 1.095 (>0, so it is compulsory) |
| 866 | G863 | Ring size 'US 7' has a space — expected 'US7' |
| 867 | D864 | Design Number blank while TDW = 1.025 (>0, so it is compulsory) |
| 867 | G864 | Ring size 'US 7' has a space — expected 'US7' |
| 868 | D865 | Design Number blank while TDW = 2.065 (>0, so it is compulsory) |
| 869 | D866 | Design Number blank while TDW = 2.86 (>0, so it is compulsory) |
| 870 | D867 | Design Number blank while TDW = 3.105 (>0, so it is compulsory) |
| 871 | D868 | Design Number blank while TDW = 3.195 (>0, so it is compulsory) |
| 872 | D869 | Design Number blank while TDW = 2.1 (>0, so it is compulsory) |
| 873 | D870 | Design Number blank while TDW = 2.64 (>0, so it is compulsory) |
| 874 | D871 | Design Number blank while TDW = 2.105 (>0, so it is compulsory) |
| 875 | D872 | Design Number blank while TDW = 1.52 (>0, so it is compulsory) |
| 876 | D873 | Design Number blank while TDW = 1.21 (>0, so it is compulsory) |
| 876 | G873 | Ring size 'US 7' has a space — expected 'US7' |
| 877 | D874 | Design Number blank while TDW = 1.255 (>0, so it is compulsory) |
| 877 | G874 | Ring size 'US 7' has a space — expected 'US7' |
| 878 | D875 | Design Number blank while TDW = 1.05 (>0, so it is compulsory) |
| 878 | G875 | Ring size 'US 7' has a space — expected 'US7' |
| 879 | D876 | Design Number blank while TDW = 1.09 (>0, so it is compulsory) |
| 879 | G876 | Ring size 'US 7' has a space — expected 'US7' |
| 880 | D877 | Design Number blank while TDW = 4.2 (>0, so it is compulsory) |
| 880 | G877 | Ring size 'US 7' has a space — expected 'US7' |
| 881 | D878 | Design Number blank while TDW = 1.04 (>0, so it is compulsory) |
| 881 | G878 | Ring size 'US 7' has a space — expected 'US7' |
| 882 | D879 | Design Number blank while TDW = 1.2 (>0, so it is compulsory) |
| 882 | G879 | Ring size 'US  7' has a space — expected 'US7' |
| 883 | D880 | Design Number blank while TDW = 39.79 (>0, so it is compulsory) |
| 883 | G880 | Ring size 'US 7' has a space — expected 'US7' |
| 884 | D881 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 884 | G881 | Ring size 'US 7' has a space — expected 'US7' |
| 885 | D882 | Design Number blank while TDW = 1.08 (>0, so it is compulsory) |
| 885 | G882 | Ring size 'US 7' has a space — expected 'US7' |
| 886 | D883 | Design Number blank while TDW = 1.2 (>0, so it is compulsory) |
| 886 | G883 | Ring size 'US 7' has a space — expected 'US7' |
| 887 | D884 | Design Number blank while TDW = 1.105 (>0, so it is compulsory) |
| 887 | G884 | Ring size 'US 7' has a space — expected 'US7' |
| 888 | D885 | Design Number blank while TDW = 1.26 (>0, so it is compulsory) |
| 888 | G885 | Ring size 'US 7' has a space — expected 'US7' |
| 889 | D886 | Design Number blank while TDW = 75.43 (>0, so it is compulsory) |
| 890 | D887 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 891 | D888 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 892 | D889 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 893 | D890 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 894 | D891 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 895 | D892 | Design Number blank while TDW = 1.27 (>0, so it is compulsory) |
| 895 | G892 | Ring size 'US 7' has a space — expected 'US7' |
| 896 | D893 | Design Number blank while TDW = 1.99 (>0, so it is compulsory) |
| 896 | G893 | Ring size 'US 7' has a space — expected 'US7' |
| 897 | D894 | Design Number blank while TDW = 2.03 (>0, so it is compulsory) |
| 897 | G894 | Ring size 'US 7' has a space — expected 'US7' |
| 898 | D895 | Design Number blank while TDW = 1.26 (>0, so it is compulsory) |
| 898 | G895 | Ring size 'US 7' has a space — expected 'US7' |
| 899 | D896 | Design Number blank while TDW = 2.04 (>0, so it is compulsory) |
| 899 | G896 | Ring size 'US 7' has a space — expected 'US7' |
| 900 | D897 | Design Number blank while TDW = 2.11 (>0, so it is compulsory) |
| 900 | G897 | Ring size 'US 7' has a space — expected 'US7' |
| 901 | D898 | Design Number blank while TDW = 2.05 (>0, so it is compulsory) |
| 901 | G898 | Ring size 'US 7' has a space — expected 'US7' |
| 902 | D899 | Design Number blank while TDW = 9.15 (>0, so it is compulsory) |
| 903 | D900 | Design Number blank while TDW = 110.429 (>0, so it is compulsory) |
| 904 | D901 | Design Number blank while TDW = 38.53 (>0, so it is compulsory) |
| 905 | D902 | Design Number blank while TDW = 105.744 (>0, so it is compulsory) |
| 906 | D903 | Design Number blank while TDW = 20.87 (>0, so it is compulsory) |
| 907 | D904 | Design Number blank while TDW = 1.0 (>0, so it is compulsory) |
| 907 | G904 | Ring size 'US 7' has a space — expected 'US7' |
| 908 | D905 | Design Number blank while TDW = 2.65 (>0, so it is compulsory) |
| 908 | G905 | Ring size 'US 7' has a space — expected 'US7' |
| 909 | D906 | Design Number blank while TDW = 1.44 (>0, so it is compulsory) |
| 909 | G906 | Ring size 'US 7' has a space — expected 'US7' |
| 910 | D907 | Design Number blank while TDW = 1.19 (>0, so it is compulsory) |
| 910 | G907 | Ring size 'US 7' has a space — expected 'US7' |
| 911 | D908 | Design Number blank while TDW = 1.04 (>0, so it is compulsory) |
| 911 | G908 | Ring size 'US 7' has a space — expected 'US7' |
| 912 | D909 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 912 | G909 | Ring size 'US 7' has a space — expected 'US7' |
| 913 | D910 | Design Number blank while TDW = 1.0 (>0, so it is compulsory) |
| 913 | G910 | Ring size 'US 7' has a space — expected 'US7' |
| 914 | D911 | Design Number blank while TDW = 2.32 (>0, so it is compulsory) |
| 914 | G911 | Ring size 'US 7' has a space — expected 'US7' |
| 915 | D912 | Design Number blank while TDW = 1.48 (>0, so it is compulsory) |
| 915 | G912 | Ring size 'US 7' has a space — expected 'US7' |
| 916 | D913 | Design Number blank while TDW = 1.36 (>0, so it is compulsory) |
| 916 | G913 | Ring size 'US 7' has a space — expected 'US7' |
| 917 | D914 | Design Number blank while TDW = 3.22 (>0, so it is compulsory) |
| 917 | G914 | Ring size 'US 7' has a space — expected 'US7' |
| 918 | D915 | Design Number blank while TDW = 1.34 (>0, so it is compulsory) |
| 918 | G915 | Ring size 'US 7' has a space — expected 'US7' |
| 919 | D916 | Design Number blank while TDW = 2.81 (>0, so it is compulsory) |
| 919 | G916 | Ring size 'US 7' has a space — expected 'US7' |
| 920 | D917 | Design Number blank while TDW = 0.97 (>0, so it is compulsory) |
| 920 | G917 | Ring size 'US 7' has a space — expected 'US7' |
| 921 | D918 | Design Number blank while TDW = 1.19 (>0, so it is compulsory) |
| 921 | G918 | Ring size 'US 7' has a space — expected 'US7' |
| 922 | D919 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 922 | G919 | Ring size 'US 7' has a space — expected 'US7' |
| 923 | D920 | Design Number blank while TDW = 1.07 (>0, so it is compulsory) |
| 923 | G920 | Ring size 'US 7' has a space — expected 'US7' |
| 924 | D921 | Design Number blank while TDW = 1.08 (>0, so it is compulsory) |
| 924 | G921 | Ring size 'US 7' has a space — expected 'US7' |
| 925 | D922 | Design Number blank while TDW = 2.73 (>0, so it is compulsory) |
| 925 | G922 | Ring size 'US 7' has a space — expected 'US7' |
| 926 | D923 | Design Number blank while TDW = 1.18 (>0, so it is compulsory) |
| 926 | G923 | Ring size 'US 7' has a space — expected 'US7' |
| 927 | D924 | Design Number blank while TDW = 2.71 (>0, so it is compulsory) |
| 927 | G924 | Ring size 'US 7' has a space — expected 'US7' |
| 928 | D925 | Design Number blank while TDW = 2.92 (>0, so it is compulsory) |
| 929 | D926 | Design Number blank while TDW = 2.46 (>0, so it is compulsory) |
| 929 | G926 | Ring size 'US 7' has a space — expected 'US7' |
| 930 | D927 | Design Number blank while TDW = 2.52 (>0, so it is compulsory) |
| 930 | G927 | Ring size 'US 7' has a space — expected 'US7' |
| 931 | D928 | Design Number blank while TDW = 1.14 (>0, so it is compulsory) |
| 931 | G928 | Ring size 'US 7' has a space — expected 'US7' |
| 932 | D929 | Design Number blank while TDW = 15.83 (>0, so it is compulsory) |
| 932 | F929 | Gold Details '14 WHITE' — no 14KT/18KT found |
| 933 | D930 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 934 | D931 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 935 | D932 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 936 | D933 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 937 | D934 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 938 | D935 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 939 | D936 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 940 | D937 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 941 | D938 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 942 | D939 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 943 | D940 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 944 | D941 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 945 | D942 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 946 | D943 | Design Number blank while TDW = 6.91 (>0, so it is compulsory) |
| 947 | D944 | Design Number blank while TDW = 6.9 (>0, so it is compulsory) |
| 948 | D945 | Design Number blank while TDW = 6.96 (>0, so it is compulsory) |
| 949 | D946 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 950 | D947 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 951 | D948 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 952 | D949 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 953 | D950 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 954 | D951 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 955 | D952 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 956 | D953 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 957 | D954 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 958 | D955 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 959 | D956 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 960 | D957 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 961 | D958 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 962 | D959 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 963 | D960 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 964 | D961 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 965 | D962 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 966 | D963 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 967 | D964 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 968 | D965 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 969 | D966 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 970 | D967 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 971 | D968 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 972 | D969 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 973 | D970 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 974 | D971 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 975 | D972 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 976 | D973 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 977 | D974 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 978 | D975 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 979 | D976 | Design Number blank while TDW = 10.15 (>0, so it is compulsory) |
| 980 | D977 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 981 | D978 | Design Number blank while TDW = 10.15 (>0, so it is compulsory) |
| 982 | D979 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 983 | D980 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 984 | D981 | Design Number blank while TDW = 10.15 (>0, so it is compulsory) |
| 985 | D982 | Design Number blank while TDW = 0.82 (>0, so it is compulsory) |
| 986 | D983 | Design Number blank while TDW = 15.25 (>0, so it is compulsory) |
| 987 | D984 | Design Number blank while TDW = 15.24 (>0, so it is compulsory) |
| 988 | D985 | Design Number blank while TDW = 15.31 (>0, so it is compulsory) |
| 989 | D986 | Design Number blank while TDW = 15.29 (>0, so it is compulsory) |
| 990 | D987 | Design Number blank while TDW = 15.83 (>0, so it is compulsory) |
| 991 | D988 | Design Number blank while TDW = 44.73 (>0, so it is compulsory) |
| 992 | D989 | Design Number blank while TDW = 5.29 (>0, so it is compulsory) |
| 993 | D990 | Design Number blank while TDW = 32.77 (>0, so it is compulsory) |
| 994 | D991 | Design Number blank while TDW = 8.21 (>0, so it is compulsory) |
| 995 | D992 | Design Number blank while TDW = 12.3 (>0, so it is compulsory) |
| 996 | D993 | Design Number blank while TDW = 12.4 (>0, so it is compulsory) |
| 997 | D994 | Design Number blank while TDW = 12.37 (>0, so it is compulsory) |
| 998 | D995 | Design Number blank while TDW = 12.3 (>0, so it is compulsory) |
| 999 | D996 | Design Number blank while TDW = 12.3 (>0, so it is compulsory) |
| 1000 | D997 | Design Number blank while TDW = 12.35 (>0, so it is compulsory) |
| 1001 | D998 | Design Number blank while TDW = 12.25 (>0, so it is compulsory) |
| 1001 | I998 | Net 12.74 exceeds gross 12.19 while TDW = 12.25. With diamonds set, net must be less than gross |
| 1002 | D999 | Design Number blank while TDW = 13.61 (>0, so it is compulsory) |
| C1003 | D1000 | Design Number blank while TDW = 11.85 (>0, so it is compulsory) |
| C1004 | D1001 | Design Number blank while TDW = 13.33 (>0, so it is compulsory) |
| 1005 | D1002 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1006 | D1003 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1007 | D1004 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 1008 | D1005 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1009 | D1006 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1010 | D1007 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1011 | D1008 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1012 | D1009 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1013 | D1010 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 1014 | D1011 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 1015 | D1012 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1016 | D1013 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1017 | D1014 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1018 | D1015 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 1019 | D1016 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1020 | D1017 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1021 | D1018 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1022 | D1019 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1023 | D1020 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1024 | D1021 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1025 | D1022 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 1026 | D1023 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1027 | D1024 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 1028 | D1025 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1029 | D1026 | Design Number blank while TDW = 6.92 (>0, so it is compulsory) |
| 1030 | D1027 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1031 | D1028 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1032 | D1029 | Design Number blank while TDW = 30.76 (>0, so it is compulsory) |
| 1033 | D1030 | Design Number blank while TDW = 25.56 (>0, so it is compulsory) |
| 1034 | D1031 | Design Number blank while TDW = 29.78 (>0, so it is compulsory) |
| 1035 | D1032 | Design Number blank while TDW = 15.87 (>0, so it is compulsory) |
| 1036 | D1033 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1037 | D1034 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1038 | D1035 | Design Number blank while TDW = 2.44 (>0, so it is compulsory) |
| 1039 | D1036 | Design Number blank while TDW = 2.41 (>0, so it is compulsory) |
| 1040 | D1037 | Design Number blank while TDW = 2.43 (>0, so it is compulsory) |
| 1040 | G1037 | Ring size 'US 7' has a space — expected 'US7' |
| 1041 | D1038 | Design Number blank while TDW = 2.51 (>0, so it is compulsory) |
| 1041 | G1038 | Ring size 'US 7' has a space — expected 'US7' |
| 1042 | D1039 | Design Number blank while TDW = 2.43 (>0, so it is compulsory) |
| 1042 | G1039 | Ring size 'US 7' has a space — expected 'US7' |
| 1043 | D1040 | Design Number blank while TDW = 2.47 (>0, so it is compulsory) |
| 1043 | G1040 | Ring size 'US 7' has a space — expected 'US7' |
| 1044 | D1041 | Design Number blank while TDW = 2.51 (>0, so it is compulsory) |
| 1044 | G1041 | Ring size 'US 7' has a space — expected 'US7' |
| 1045 | D1042 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1046 | D1043 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1047 | D1044 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1048 | D1045 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1049 | D1046 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1050 | D1047 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1051 | D1048 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1052 | D1049 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1053 | D1050 | Design Number blank while TDW = 3.0 (>0, so it is compulsory) |
| 1054 | D1051 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1055 | D1052 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1056 | D1053 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1057 | D1054 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1058 | D1055 | Design Number blank while TDW = 3.0 (>0, so it is compulsory) |
| 1059 | D1056 | Design Number blank while TDW = 3.0 (>0, so it is compulsory) |
| 1060 | D1057 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1061 | D1058 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1062 | D1059 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1063 | D1060 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1064 | D1061 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1065 | D1062 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1066 | D1063 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1067 | D1064 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1068 | D1065 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1069 | D1066 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1070 | D1067 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1071 | D1068 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1072 | D1069 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1073 | D1070 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1074 | D1071 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1075 | D1072 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1076 | D1073 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1077 | D1074 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1078 | D1075 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1079 | D1076 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1080 | D1077 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1081 | D1078 | Design Number blank while TDW = 10.41 (>0, so it is compulsory) |
| 1082 | D1079 | Design Number blank while TDW = 10.41 (>0, so it is compulsory) |
| 1083 | D1080 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1084 | D1081 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1085 | D1082 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1086 | D1083 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1087 | D1084 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1088 | D1085 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1089 | D1086 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1090 | D1087 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1091 | D1088 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1092 | D1089 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1093 | D1090 | Design Number blank while TDW = 34.425 (>0, so it is compulsory) |
| 1094 | D1091 | Design Number blank while TDW = 29.78 (>0, so it is compulsory) |
| 1095 | D1092 | Design Number blank while TDW = 23.37 (>0, so it is compulsory) |
| 1096 | D1093 | Design Number blank while TDW = 10.59 (>0, so it is compulsory) |
| 1097 | D1094 | Design Number blank while TDW = 10.46 (>0, so it is compulsory) |
| 1098 | D1095 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1099 | D1096 | Design Number blank while TDW = 10.2 (>0, so it is compulsory) |
| 1100 | D1097 | Design Number blank while TDW = 10.21 (>0, so it is compulsory) |
| 1101 | D1098 | Design Number blank while TDW = 15.29 (>0, so it is compulsory) |
| 1102 | D1099 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1103 | D1100 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1104 | D1101 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1105 | D1102 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1106 | D1103 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1107 | D1104 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1108 | D1105 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1109 | D1106 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1110 | D1107 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1111 | D1108 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1112 | D1109 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1113 | D1110 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1114 | D1111 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1115 | D1112 | Design Number blank while TDW = 6.08 (>0, so it is compulsory) |
| 1116 | D1113 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1117 | D1114 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1118 | D1115 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1119 | D1116 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1120 | D1117 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1121 | D1118 | Design Number blank while TDW = 6.1 (>0, so it is compulsory) |
| 1122 | D1119 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1123 | D1120 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1124 | D1121 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1125 | D1122 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1126 | D1123 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1127 | D1124 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1128 | D1125 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1129 | D1126 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| 1130 | D1127 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1131 | D1128 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1132 | D1129 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1133 | D1130 | Design Number blank while TDW = 10.63 (>0, so it is compulsory) |
| 1134 | D1131 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1135 | D1132 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1136 | D1133 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1137 | D1134 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1138 | D1135 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1139 | D1136 | Design Number blank while TDW = 14.89 (>0, so it is compulsory) |
| 1139 | R1136 | Product Code '0.0' is not on the Price List |
| 1140 | D1137 | Design Number blank while TDW = 14.99 (>0, so it is compulsory) |
| 1141 | D1138 | Design Number blank while TDW = 7.25 (>0, so it is compulsory) |
| 1142 | D1139 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1143 | D1140 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1144 | D1141 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1145 | D1142 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1146 | D1143 | Design Number blank while TDW = 3.0 (>0, so it is compulsory) |
| 1147 | D1144 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1148 | D1145 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1149 | D1146 | Design Number blank while TDW = 3.0 (>0, so it is compulsory) |
| 1150 | D1147 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1151 | D1148 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1152 | D1149 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1153 | D1150 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1154 | D1151 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1155 | F1152 | Gold Details 'SILVER' — no 14KT/18KT found |
| 1155 | H1152 | GROSS WEIGHT blank |
| 1155 | I1152 | NET WEIGHT blank |
| 1156 | D1153 | Design Number blank while TDW = 17.45 (>0, so it is compulsory) |
| 1157 | D1154 | Design Number blank while TDW = 38.32 (>0, so it is compulsory) |
| 1158 | D1155 | Design Number blank while TDW = 35.39 (>0, so it is compulsory) |
| 1159 | D1156 | Design Number blank while TDW = 14.435 (>0, so it is compulsory) |
| 1160 | D1157 | Design Number blank while TDW = 1.08 (>0, so it is compulsory) |
| 1160 | G1157 | Ring size 'US 7' has a space — expected 'US7' |
| 1161 | D1158 | Design Number blank while TDW = 1.092 (>0, so it is compulsory) |
| 1161 | G1158 | Ring size 'US 7' has a space — expected 'US7' |
| 1162 | D1159 | Design Number blank while TDW = 1.082 (>0, so it is compulsory) |
| 1162 | G1159 | Ring size 'US 7' has a space — expected 'US7' |
| 1163 | D1160 | Design Number blank while TDW = 1.05 (>0, so it is compulsory) |
| 1163 | G1160 | Ring size 'US 7' has a space — expected 'US7' |
| 1164 | D1161 | Design Number blank while TDW = 1.89 (>0, so it is compulsory) |
| 1164 | G1161 | Ring size 'US 7' has a space — expected 'US7' |
| 1165 | D1162 | Design Number blank while TDW = 1.095 (>0, so it is compulsory) |
| 1165 | G1162 | Ring size 'US 7' has a space — expected 'US7' |
| 1166 | D1163 | Design Number blank while TDW = 1.107 (>0, so it is compulsory) |
| 1166 | G1163 | Ring size 'US 7' has a space — expected 'US7' |
| 1167 | D1164 | Design Number blank while TDW = 1.09 (>0, so it is compulsory) |
| 1167 | G1164 | Ring size 'US 7' has a space — expected 'US7' |
| 1168 | D1165 | Design Number blank while TDW = 1.08 (>0, so it is compulsory) |
| 1168 | G1165 | Ring size 'US 7' has a space — expected 'US7' |
| 1169 | D1166 | Design Number blank while TDW = 1.08 (>0, so it is compulsory) |
| 1169 | G1166 | Ring size 'US 7' has a space — expected 'US7' |
| 1170 | D1167 | Design Number blank while TDW = 9.2 (>0, so it is compulsory) |
| 1171 | D1168 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1172 | D1169 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1173 | D1170 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1174 | D1171 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1175 | D1172 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 1176 | D1173 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1177 | D1174 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1178 | D1175 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1179 | D1176 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1180 | D1177 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1181 | D1178 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1182 | D1179 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1183 | D1180 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1184 | D1181 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1185 | D1182 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1186 | D1183 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1187 | D1184 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1188 | D1185 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1189 | D1186 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1190 | D1187 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1191 | D1188 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1192 | D1189 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1193 | D1190 | Design Number blank while TDW = 10.19 (>0, so it is compulsory) |
| 1194 | D1191 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1195 | D1192 | Design Number blank while TDW = 10.16 (>0, so it is compulsory) |
| 1196 | D1193 | Design Number blank while TDW = 10.14 (>0, so it is compulsory) |
| 1197 | D1194 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1198 | D1195 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1199 | D1196 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1200 | D1197 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1201 | D1198 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1202 | D1199 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1203 | D1200 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 1204 | D1201 | Design Number blank while TDW = 9.96 (>0, so it is compulsory) |
| 1205 | D1202 | Design Number blank while TDW = 38.965 (>0, so it is compulsory) |
| 1206 | D1203 | Design Number blank while TDW = 2.235 (>0, so it is compulsory) |
| 1206 | G1203 | Ring size 'US 7' has a space — expected 'US7' |
| 1207 | D1204 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1208 | D1205 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1209 | D1206 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1210 | D1207 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1211 | D1208 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1212 | D1209 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1213 | D1210 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1214 | D1211 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1215 | D1212 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1216 | D1213 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1217 | D1214 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1218 | D1215 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1219 | D1216 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1220 | D1217 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1221 | D1218 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1222 | D1219 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1223 | D1220 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1224 | D1221 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1225 | D1222 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1226 | D1223 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1227 | D1224 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1228 | D1225 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1229 | D1226 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1230 | D1227 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1231 | D1228 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1232 | D1229 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1233 | D1230 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1234 | D1231 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1235 | D1232 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1236 | D1233 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1237 | D1234 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1238 | D1235 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1239 | D1236 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1240 | D1237 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1241 | D1238 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1242 | D1239 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1243 | D1240 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1244 | D1241 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1245 | D1242 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1246 | D1243 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1247 | D1244 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1248 | D1245 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1249 | D1246 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1250 | D1247 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1251 | D1248 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1252 | D1249 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1253 | D1250 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1254 | D1251 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1255 | D1252 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1256 | D1253 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1257 | D1254 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1258 | D1255 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1259 | D1256 | Design Number blank while TDW = 1.96 (>0, so it is compulsory) |
| 1259 | G1256 | Ring size 'US 7' has a space — expected 'US7' |
| 1260 | D1257 | Design Number blank while TDW = 29.425 (>0, so it is compulsory) |
| 1261 | D1258 | Design Number blank while TDW = 16.61 (>0, so it is compulsory) |
| 1262 | D1259 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1263 | D1260 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1264 | D1261 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1265 | D1262 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1266 | D1263 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1267 | D1264 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1268 | D1265 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1269 | D1266 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1270 | D1267 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1271 | D1268 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1272 | D1269 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1273 | D1270 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1274 | D1271 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1275 | D1272 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1276 | D1273 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1277 | D1274 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1278 | D1275 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1279 | D1276 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1280 | D1277 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1281 | D1278 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1282 | D1279 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1283 | D1280 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1284 | D1281 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1285 | D1282 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1286 | D1283 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1287 | D1284 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1288 | D1285 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1289 | D1286 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1290 | D1287 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1291 | D1288 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1292 | D1289 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1293 | D1290 | Design Number blank while TDW = 34.49 (>0, so it is compulsory) |
| 1294 | D1291 | Design Number blank while TDW = 36.145 (>0, so it is compulsory) |
| 1295 | D1292 | Design Number blank while TDW = 36.45 (>0, so it is compulsory) |
| 1296 | D1293 | Design Number blank while TDW = 30.155 (>0, so it is compulsory) |
| 1297 | D1294 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1297 | G1294 | Ring size 'US 7' has a space — expected 'US7' |
| 1298 | D1295 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1298 | G1295 | Ring size 'US 7' has a space — expected 'US7' |
| 1299 | D1296 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1299 | G1296 | Ring size 'US 7' has a space — expected 'US7' |
| 1300 | D1297 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1300 | G1297 | Ring size 'US 7' has a space — expected 'US7' |
| 1301 | D1298 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1301 | G1298 | Ring size 'US 7' has a space — expected 'US7' |
| 1302 | D1299 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1302 | G1299 | Ring size 'US 7' has a space — expected 'US7' |
| 1303 | D1300 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1303 | G1300 | Ring size 'US 7' has a space — expected 'US7' |
| 1304 | D1301 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1304 | G1301 | Ring size 'US 7' has a space — expected 'US7' |
| 1305 | D1302 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1305 | G1302 | Ring size 'US 7' has a space — expected 'US7' |
| 1306 | D1303 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1306 | G1303 | Ring size 'US 7' has a space — expected 'US7' |
| 1307 | D1304 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1307 | G1304 | Ring size 'US 7' has a space — expected 'US7' |
| 1308 | D1305 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1308 | G1305 | Ring size 'US 7' has a space — expected 'US7' |
| 1309 | D1306 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1309 | G1306 | Ring size 'US 7' has a space — expected 'US7' |
| 1310 | D1307 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1310 | G1307 | Ring size 'US 7' has a space — expected 'US7' |
| 1311 | D1308 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1311 | G1308 | Ring size 'US 7' has a space — expected 'US7' |
| 1312 | D1309 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1312 | G1309 | Ring size 'US 7' has a space — expected 'US7' |
| 1313 | D1310 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1313 | G1310 | Ring size 'US 7' has a space — expected 'US7' |
| 1314 | D1311 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1314 | G1311 | Ring size 'US 7' has a space — expected 'US7' |
| 1315 | D1312 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1315 | G1312 | Ring size 'US 7' has a space — expected 'US7' |
| 1316 | D1313 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1316 | G1313 | Ring size 'US 7' has a space — expected 'US7' |
| 1317 | D1314 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1317 | G1314 | Ring size 'US 7' has a space — expected 'US7' |
| 1318 | D1315 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1318 | G1315 | Ring size 'US 7' has a space — expected 'US7' |
| 1319 | D1316 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1319 | G1316 | Ring size 'US 7' has a space — expected 'US7' |
| 1320 | D1317 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1320 | G1317 | Ring size 'US 7' has a space — expected 'US7' |
| 1321 | D1318 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1321 | G1318 | Ring size 'US 7' has a space — expected 'US7' |
| 1322 | D1319 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1322 | G1319 | Ring size 'US 7' has a space — expected 'US7' |
| 1323 | D1320 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1323 | G1320 | Ring size 'US 7' has a space — expected 'US7' |
| 1324 | D1321 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1324 | G1321 | Ring size 'US 7' has a space — expected 'US7' |
| 1325 | D1322 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1325 | G1322 | Ring size 'US 7' has a space — expected 'US7' |
| 1326 | D1323 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1326 | G1323 | Ring size 'US 7' has a space — expected 'US7' |
| 1327 | D1324 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1327 | G1324 | Ring size 'US 7' has a space — expected 'US7' |
| 1328 | D1325 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1328 | G1325 | Ring size 'US 7' has a space — expected 'US7' |
| 1329 | D1326 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1329 | G1326 | Ring size 'US 7' has a space — expected 'US7' |
| 1330 | D1327 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1330 | G1327 | Ring size 'US 7' has a space — expected 'US7' |
| 1331 | D1328 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1331 | G1328 | Ring size 'US 7' has a space — expected 'US7' |
| 1332 | D1329 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 1332 | G1329 | Ring size 'US 7' has a space — expected 'US7' |
| 1333 | D1330 | Design Number blank while TDW = 2.01 (>0, so it is compulsory) |
| 1333 | G1330 | Ring size 'US 7' has a space — expected 'US7' |
| 1334 | D1331 | Design Number blank while TDW = 5.92 (>0, so it is compulsory) |
| 1335 | D1332 | Design Number blank while TDW = 7.115 (>0, so it is compulsory) |
| 1336 | D1333 | Design Number blank while TDW = 38.81 (>0, so it is compulsory) |
| 1337 | D1334 | Design Number blank while TDW = 37.43 (>0, so it is compulsory) |
| 1338 | D1335 | Design Number blank while TDW = 23.78 (>0, so it is compulsory) |
| 1339 | D1336 | Design Number blank while TDW = 23.85 (>0, so it is compulsory) |
| 1340 | D1337 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1341 | D1338 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1342 | D1339 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1343 | D1340 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1344 | D1341 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1345 | D1342 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1346 | D1343 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1347 | D1344 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1348 | D1345 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1349 | D1346 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1350 | D1347 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1351 | D1348 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1352 | D1349 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1353 | D1350 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1353 | G1350 | Ring size 'US 7' has a space — expected 'US7' |
| 1354 | D1351 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1354 | G1351 | Ring size 'US 7' has a space — expected 'US7' |
| 1355 | D1352 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1355 | G1352 | Ring size 'US 7' has a space — expected 'US7' |
| 1356 | D1353 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1356 | G1353 | Ring size 'US 7' has a space — expected 'US7' |
| 1357 | D1354 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1357 | G1354 | Ring size 'US 7' has a space — expected 'US7' |
| 1358 | D1355 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1358 | G1355 | Ring size 'US 7' has a space — expected 'US7' |
| 1359 | D1356 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1359 | G1356 | Ring size 'US 7' has a space — expected 'US7' |
| 1360 | D1357 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1360 | G1357 | Ring size 'US 7' has a space — expected 'US7' |
| 1361 | D1358 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1361 | G1358 | Ring size 'US 7' has a space — expected 'US7' |
| 1362 | D1359 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1362 | G1359 | Ring size 'US 7' has a space — expected 'US7' |
| 1363 | D1360 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1363 | G1360 | Ring size 'US 7' has a space — expected 'US7' |
| 1364 | D1361 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1364 | G1361 | Ring size 'US 7' has a space — expected 'US7' |
| 1365 | D1362 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1365 | G1362 | Ring size 'US 7' has a space — expected 'US7' |
| 1366 | D1363 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1366 | G1363 | Ring size 'US 7' has a space — expected 'US7' |
| 1367 | D1364 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1367 | G1364 | Ring size 'US 7' has a space — expected 'US7' |
| 1368 | D1365 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1368 | G1365 | Ring size 'US 7' has a space — expected 'US7' |
| 1369 | D1366 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1369 | G1366 | Ring size 'US 7' has a space — expected 'US7' |
| 1370 | D1367 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1370 | G1367 | Ring size 'US 7' has a space — expected 'US7' |
| 1371 | D1368 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1371 | G1368 | Ring size 'US 7' has a space — expected 'US7' |
| 1372 | D1369 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1372 | G1369 | Ring size 'US 7' has a space — expected 'US7' |
| 1373 | D1370 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1373 | G1370 | Ring size 'US 7' has a space — expected 'US7' |
| 1374 | D1371 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1374 | G1371 | Ring size 'US 7' has a space — expected 'US7' |
| 1375 | D1372 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1375 | G1372 | Ring size 'US 7' has a space — expected 'US7' |
| 1376 | D1373 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1376 | G1373 | Ring size 'US 7' has a space — expected 'US7' |
| 1377 | D1374 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1377 | G1374 | Ring size 'US 7' has a space — expected 'US7' |
| 1378 | D1375 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1378 | G1375 | Ring size 'US 7' has a space — expected 'US7' |
| 1379 | D1376 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1379 | G1376 | Ring size 'US 7' has a space — expected 'US7' |
| 1380 | D1377 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1380 | G1377 | Ring size 'US 7' has a space — expected 'US7' |
| 1381 | D1378 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1381 | G1378 | Ring size 'US 7' has a space — expected 'US7' |
| 1382 | D1379 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1382 | G1379 | Ring size 'US 7' has a space — expected 'US7' |
| 1383 | D1380 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1383 | G1380 | Ring size 'US 7' has a space — expected 'US7' |
| 1384 | D1381 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1384 | G1381 | Ring size 'US 7' has a space — expected 'US7' |
| 1385 | D1382 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1385 | G1382 | Ring size 'US 7' has a space — expected 'US7' |
| 1386 | D1383 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1386 | G1383 | Ring size 'US 7' has a space — expected 'US7' |
| 1387 | D1384 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1387 | G1384 | Ring size 'US 7' has a space — expected 'US7' |
| 1388 | D1385 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1388 | G1385 | Ring size 'US 7' has a space — expected 'US7' |
| 1389 | D1386 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1389 | G1386 | Ring size 'US 7' has a space — expected 'US7' |
| 1390 | D1387 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1390 | G1387 | Ring size 'US 7' has a space — expected 'US7' |
| 1391 | D1388 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1391 | G1388 | Ring size 'US 7' has a space — expected 'US7' |
| 1392 | D1389 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1392 | G1389 | Ring size 'US 7' has a space — expected 'US7' |
| 1393 | D1390 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1393 | G1390 | Ring size 'US 7' has a space — expected 'US7' |
| 1394 | D1391 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1394 | G1391 | Ring size 'US 7' has a space — expected 'US7' |
| 1395 | D1392 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1395 | G1392 | Ring size 'US 7' has a space — expected 'US7' |
| 1396 | D1393 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1396 | G1393 | Ring size 'US 7' has a space — expected 'US7' |
| 1397 | D1394 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1397 | G1394 | Ring size 'US 7' has a space — expected 'US7' |
| 1398 | D1395 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1398 | G1395 | Ring size 'US 7' has a space — expected 'US7' |
| 1399 | D1396 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1399 | G1396 | Ring size 'US 7' has a space — expected 'US7' |
| 1400 | D1397 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1400 | G1397 | Ring size 'US 7' has a space — expected 'US7' |
| 1401 | D1398 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1401 | G1398 | Ring size 'US 7' has a space — expected 'US7' |
| 1402 | D1399 | Design Number blank while TDW = 1.59 (>0, so it is compulsory) |
| 1402 | G1399 | Ring size 'US 7' has a space — expected 'US7' |
| 1403 | D1400 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1403 | G1400 | Ring size 'US 7' has a space — expected 'US7' |
| 1404 | D1401 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1404 | G1401 | Ring size 'US 7' has a space — expected 'US7' |
| 1405 | D1402 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1405 | G1402 | Ring size 'US 7' has a space — expected 'US7' |
| 1406 | D1403 | Design Number blank while TDW = 3.12 (>0, so it is compulsory) |
| 1406 | G1403 | Ring size 'US 7' has a space — expected 'US7' |
| 1407 | D1404 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1407 | G1404 | Ring size 'US 7' has a space — expected 'US7' |
| 1408 | D1405 | Design Number blank while TDW = 4.03 (>0, so it is compulsory) |
| 1408 | G1405 | Ring size 'US 7' has a space — expected 'US7' |
| 1409 | D1406 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1409 | G1406 | Ring size 'US 7' has a space — expected 'US7' |
| 1410 | D1407 | Design Number blank while TDW = 4.04 (>0, so it is compulsory) |
| 1410 | G1407 | Ring size 'US 7' has a space — expected 'US7' |
| 1411 | D1408 | Design Number blank while TDW = 1.6 (>0, so it is compulsory) |
| 1411 | G1408 | Ring size 'US 7' has a space — expected 'US7' |
| 1412 | D1409 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1413 | D1410 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1414 | D1411 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1415 | D1412 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1416 | D1413 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1417 | D1414 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1418 | D1415 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1419 | D1416 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1420 | D1417 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1421 | D1418 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1422 | D1419 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1423 | D1420 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1424 | D1421 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1425 | D1422 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1426 | D1423 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1427 | D1424 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1428 | D1425 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1429 | D1426 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1430 | D1427 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1431 | D1428 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1432 | D1429 | Design Number blank while TDW = 9.275 (>0, so it is compulsory) |
| 1433 | D1430 | Design Number blank while TDW = 14.55 (>0, so it is compulsory) |
| 1434 | D1431 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 1435 | D1432 | Design Number blank while TDW = 4.4 (>0, so it is compulsory) |
| 1435 | G1432 | Ring size 'US 14' has a space — expected 'US14' |
| 1436 | D1433 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1437 | D1434 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1438 | D1435 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1439 | D1436 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1440 | D1437 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1441 | D1438 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1442 | D1439 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1443 | D1440 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1444 | D1441 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1445 | D1442 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1446 | D1443 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1447 | D1444 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1448 | D1445 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1449 | D1446 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1450 | D1447 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1451 | D1448 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1452 | D1449 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1453 | D1450 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1454 | D1451 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1455 | D1452 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1456 | D1453 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1457 | D1454 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1458 | D1455 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1459 | D1456 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1460 | D1457 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1461 | D1458 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1462 | D1459 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1463 | D1460 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1464 | D1461 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1465 | D1462 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1466 | D1463 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1467 | D1464 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1468 | D1465 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1469 | D1466 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1470 | D1467 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1471 | D1468 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1472 | D1469 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1473 | D1470 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1474 | D1471 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1475 | D1472 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1476 | D1473 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1477 | D1474 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1478 | D1475 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1479 | D1476 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1480 | D1477 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1481 | D1478 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1482 | D1479 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1483 | D1480 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1484 | D1481 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1485 | D1482 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1486 | D1483 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1487 | D1484 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1488 | D1485 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1489 | D1486 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1490 | D1487 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1491 | D1488 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1492 | D1489 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1493 | D1490 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1494 | D1491 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1495 | D1492 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1496 | D1493 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1497 | D1494 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1498 | D1495 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1499 | D1496 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1500 | D1497 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1501 | D1498 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1502 | D1499 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1503 | D1500 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1504 | D1501 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1505 | D1502 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1506 | D1503 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1507 | D1504 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1508 | D1505 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1509 | D1506 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1510 | D1507 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1511 | D1508 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1512 | D1509 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1513 | D1510 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1514 | D1511 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1515 | D1512 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1516 | D1513 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1517 | D1514 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1518 | D1515 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1519 | D1516 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1520 | D1517 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1521 | D1518 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1522 | D1519 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1523 | D1520 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1524 | D1521 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1525 | D1522 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1526 | D1523 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1527 | D1524 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1528 | D1525 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1529 | D1526 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1530 | D1527 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1531 | D1528 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1532 | D1529 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1533 | D1530 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1534 | D1531 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1535 | D1532 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1536 | D1533 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1537 | D1534 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1538 | D1535 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1539 | D1536 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1540 | D1537 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1541 | D1538 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1542 | D1539 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1543 | D1540 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1544 | D1541 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1545 | D1542 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1546 | D1543 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1547 | D1544 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1548 | D1545 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1549 | D1546 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1550 | D1547 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1551 | D1548 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1552 | D1549 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1553 | D1550 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1554 | D1551 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1555 | D1552 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1556 | D1553 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1557 | D1554 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1558 | D1555 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1559 | D1556 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1560 | D1557 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1561 | D1558 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1562 | D1559 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1563 | D1560 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1564 | D1561 | Design Number blank while TDW = 10.78 (>0, so it is compulsory) |
| 1565 | D1562 | Design Number blank while TDW = 10.63 (>0, so it is compulsory) |
| 1566 | D1563 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 1567 | D1564 | Design Number blank while TDW = 7.55 (>0, so it is compulsory) |
| 1568 | D1565 | Design Number blank while TDW = 16.93 (>0, so it is compulsory) |
| 1569 | D1566 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1570 | D1567 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1571 | D1568 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1572 | D1569 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1573 | D1570 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1574 | D1571 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1575 | D1572 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1576 | D1573 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1577 | D1574 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1578 | D1575 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1579 | D1576 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1580 | D1577 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1581 | D1578 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1582 | D1579 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1583 | D1580 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1584 | D1581 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1585 | D1582 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1586 | D1583 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1587 | D1584 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1588 | D1585 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1589 | D1586 | Design Number blank while TDW = 10.23 (>0, so it is compulsory) |
| 1590 | D1587 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1591 | D1588 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1592 | D1589 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1593 | D1590 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1594 | D1591 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1595 | D1592 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1596 | D1593 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1597 | D1594 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1598 | D1595 | Design Number blank while TDW = 10.28 (>0, so it is compulsory) |
| 1599 | D1596 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1600 | D1597 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1601 | D1598 | Design Number blank while TDW = 3.14 (>0, so it is compulsory) |
| 1602 | D1599 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1603 | D1600 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1604 | D1601 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1605 | D1602 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1606 | D1603 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1607 | D1604 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1608 | D1605 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1609 | D1606 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1610 | D1607 | Design Number blank while TDW = 5.5 (>0, so it is compulsory) |
| 1611 | D1608 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1612 | D1609 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1613 | D1610 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1614 | D1611 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1615 | D1612 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1616 | D1613 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1617 | D1614 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1618 | D1615 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1619 | D1616 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1620 | D1617 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1621 | D1618 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1622 | D1619 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1623 | D1620 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1624 | D1621 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1625 | D1622 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1626 | D1623 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1627 | D1624 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1628 | D1625 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1629 | D1626 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1630 | D1627 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1631 | D1628 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1632 | D1629 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1633 | D1630 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1634 | D1631 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1635 | D1632 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1636 | D1633 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1637 | D1634 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1638 | D1635 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1639 | D1636 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1640 | D1637 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1641 | D1638 | Design Number blank while TDW = 3.35 (>0, so it is compulsory) |
| 1642 | D1639 | Design Number blank while TDW = 32.61 (>0, so it is compulsory) |
| 1643 | D1640 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1644 | D1641 | Design Number blank while TDW = 2.95 (>0, so it is compulsory) |
| 1645 | D1642 | Design Number blank while TDW = 26.29 (>0, so it is compulsory) |
| 1646 | D1643 | Design Number blank while TDW = 26.73 (>0, so it is compulsory) |
| 1647 | D1644 | Design Number blank while TDW = 37.34 (>0, so it is compulsory) |
| 1648 | D1645 | Design Number blank while TDW = 33.4 (>0, so it is compulsory) |
| 1649 | D1646 | Design Number blank while TDW = 27.795 (>0, so it is compulsory) |
| 1650 | D1647 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 1651 | D1648 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 1652 | D1649 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1653 | D1650 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1654 | D1651 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1655 | D1652 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1656 | D1653 | Design Number blank while TDW = 5.5 (>0, so it is compulsory) |
| 1657 | D1654 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1658 | D1655 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1659 | D1656 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1660 | D1657 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1661 | D1658 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 1662 | D1659 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1663 | D1660 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1664 | D1661 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1665 | D1662 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1666 | D1663 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1667 | D1664 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1668 | D1665 | Design Number blank while TDW = 5.2 (>0, so it is compulsory) |
| 1669 | D1666 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1670 | D1667 | Design Number blank while TDW = 23.85 (>0, so it is compulsory) |
| 1671 | D1668 | Design Number blank while TDW = 26.8 (>0, so it is compulsory) |
| 1672 | D1669 | Design Number blank while TDW = 23.32 (>0, so it is compulsory) |
| 1673 | D1670 | Design Number blank while TDW = 16.485 (>0, so it is compulsory) |
| 1674 | D1671 | Design Number blank while TDW = 16.76 (>0, so it is compulsory) |
| 1675 | D1672 | Design Number blank while TDW = 31.81 (>0, so it is compulsory) |
| 1676 | D1673 | Design Number blank while TDW = 33.405 (>0, so it is compulsory) |
| 1677 | D1674 | Design Number blank while TDW = 10.41 (>0, so it is compulsory) |
| 1678 | D1675 | Design Number blank while TDW = 10.48 (>0, so it is compulsory) |
| 1679 | D1676 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1680 | D1677 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1681 | D1678 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1682 | D1679 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1683 | D1680 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1684 | D1681 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1685 | D1682 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1686 | D1683 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1687 | D1684 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1688 | D1685 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1689 | D1686 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1690 | D1687 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1714 | D1688 | Design Number blank while TDW = 31.87 (>0, so it is compulsory) |
| 1715 | D1689 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1716 | D1690 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1717 | D1691 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1718 | D1692 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 1719 | D1693 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1720 | D1694 | Design Number blank while TDW = 3.2 (>0, so it is compulsory) |
| 1721 | D1695 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1722 | D1696 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 1723 | D1697 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1724 | D1698 | Design Number blank while TDW = 11.06 (>0, so it is compulsory) |
| 1725 | D1699 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1726 | D1700 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1727 | D1701 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1728 | D1702 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1729 | D1703 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1730 | D1704 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1731 | D1705 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1732 | D1706 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1733 | D1707 | Design Number blank while TDW = 3.01 (>0, so it is compulsory) |
| 1734 | D1708 | Design Number blank while TDW = 10.54 (>0, so it is compulsory) |
| 1735 | D1709 | Design Number blank while TDW = 11.06 (>0, so it is compulsory) |
| 1736 | D1710 | Design Number blank while TDW = 11.06 (>0, so it is compulsory) |
| 1737 | D1711 | Design Number blank while TDW = 11.06 (>0, so it is compulsory) |
| 1738 | D1712 | Design Number blank while TDW = 11.06 (>0, so it is compulsory) |
| 1739 | D1713 | Design Number blank while TDW = 11.08 (>0, so it is compulsory) |
| 1740 | D1714 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1741 | D1715 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1742 | D1716 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1743 | D1717 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1744 | D1718 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1745 | D1719 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1746 | D1720 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1747 | D1721 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1748 | D1722 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1749 | D1723 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1750 | D1724 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 1751 | D1725 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1752 | D1726 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1753 | D1727 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1754 | D1728 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1755 | D1729 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 1756 | D1730 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1757 | D1731 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1758 | D1732 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1759 | D1733 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1760 | D1734 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1761 | D1735 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 1762 | D1736 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1763 | D1737 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 1764 | D1738 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1765 | D1739 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1766 | D1740 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1767 | D1741 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1768 | D1742 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1769 | D1743 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1770 | D1744 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 1771 | D1745 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1772 | D1746 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1773 | D1747 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1774 | D1748 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1775 | D1749 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 1776 | D1750 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1777 | D1751 | Design Number blank while TDW = 10.15 (>0, so it is compulsory) |
| 1778 | D1752 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1779 | D1753 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1780 | D1754 | Design Number blank while TDW = 10.05 (>0, so it is compulsory) |
| 1781 | D1755 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1782 | D1756 | Design Number blank while TDW = 10.0 (>0, so it is compulsory) |
| 1783 | D1757 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1784 | D1758 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1785 | D1759 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 1786 | D1760 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1787 | D1761 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1788 | D1762 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 1789 | D1763 | Design Number blank while TDW = 3.03 (>0, so it is compulsory) |
| 1790 | D1764 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1791 | D1765 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 1792 | D1766 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 1793 | D1767 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 1794 | D1768 | Design Number blank while TDW = 3.13 (>0, so it is compulsory) |
| 1795 | D1769 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1796 | D1770 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1797 | D1771 | Design Number blank while TDW = 3.09 (>0, so it is compulsory) |
| 1798 | D1772 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1799 | D1773 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 1800 | D1774 | Design Number blank while TDW = 3.04 (>0, so it is compulsory) |
| 1801 | D1775 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1802 | D1776 | Design Number blank while TDW = 15.08 (>0, so it is compulsory) |
| 1803 | D1777 | Design Number blank while TDW = 14.95 (>0, so it is compulsory) |
| 1804 | D1778 | Design Number blank while TDW = 14.95 (>0, so it is compulsory) |
| 1805 | D1779 | Design Number blank while TDW = 14.95 (>0, so it is compulsory) |
| 1806 | D1780 | Design Number blank while TDW = 14.95 (>0, so it is compulsory) |
| 1807 | D1781 | Design Number blank while TDW = 11.06 (>0, so it is compulsory) |
| 1808 | D1782 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 1809 | D1783 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 1810 | D1784 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1811 | D1785 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 1812 | D1786 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1813 | D1787 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1814 | D1788 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1815 | D1789 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1816 | D1790 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 1817 | D1791 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1818 | D1792 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1819 | D1793 | Design Number blank while TDW = 3.11 (>0, so it is compulsory) |
| 1820 | D1794 | Design Number blank while TDW = 15.25 (>0, so it is compulsory) |
| 1821 | D1795 | Design Number blank while TDW = 15.26 (>0, so it is compulsory) |
| 1822 | D1796 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1823 | D1797 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 1824 | D1798 | Design Number blank while TDW = 3.05 (>0, so it is compulsory) |
| 1825 | D1799 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1826 | D1800 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1827 | D1801 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1828 | D1802 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1829 | D1803 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1830 | D1804 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1831 | D1805 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1832 | D1806 | Design Number blank while TDW = 7.22 (>0, so it is compulsory) |
| 1833 | D1807 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1834 | D1808 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 1835 | D1809 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 1836 | D1810 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 1837 | D1811 | Design Number blank while TDW = 7.11 (>0, so it is compulsory) |
| 1838 | D1812 | Design Number blank while TDW = 7.22 (>0, so it is compulsory) |
| 1839 | D1813 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1840 | D1814 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 1841 | D1815 | Design Number blank while TDW = 7.09 (>0, so it is compulsory) |
| 1842 | D1816 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1843 | D1817 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1844 | D1818 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 1845 | D1819 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1846 | D1820 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1847 | D1821 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1848 | D1822 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 1849 | D1823 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 1850 | D1824 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 1851 | D1825 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 1852 | D1826 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1853 | D1827 | Design Number blank while TDW = 7.25 (>0, so it is compulsory) |
| 1854 | D1828 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 1855 | D1829 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1856 | D1830 | Design Number blank while TDW = 7.26 (>0, so it is compulsory) |
| 1857 | D1831 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 1858 | D1832 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1859 | D1833 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 1860 | D1834 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1861 | D1835 | Design Number blank while TDW = 7.27 (>0, so it is compulsory) |
| 1862 | D1836 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 1863 | D1837 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 1864 | D1838 | Design Number blank while TDW = 7.32 (>0, so it is compulsory) |
| 1865 | D1839 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 1866 | D1840 | Design Number blank while TDW = 7.22 (>0, so it is compulsory) |
| 1867 | D1841 | Design Number blank while TDW = 7.25 (>0, so it is compulsory) |
| 1868 | D1842 | Design Number blank while TDW = 7.22 (>0, so it is compulsory) |
| 1869 | D1843 | Design Number blank while TDW = 7.24 (>0, so it is compulsory) |
| 1870 | D1844 | Design Number blank while TDW = 7.24 (>0, so it is compulsory) |
| 1871 | D1845 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1872 | D1846 | Design Number blank while TDW = 10.4 (>0, so it is compulsory) |
| 1873 | D1847 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 1874 | D1848 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 1875 | D1849 | Design Number blank while TDW = 15.03 (>0, so it is compulsory) |
| 1876 | D1850 | Design Number blank while TDW = 15.01 (>0, so it is compulsory) |
| 1877 | D1851 | Design Number blank while TDW = 15.03 (>0, so it is compulsory) |
| 1878 | D1852 | Design Number blank while TDW = 7.42 (>0, so it is compulsory) |
| 1879 | D1853 | Design Number blank while TDW = 16.6 (>0, so it is compulsory) |
| 1880 | D1854 | Design Number blank while TDW = 15.85 (>0, so it is compulsory) |
| 1881 | D1855 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1882 | D1856 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 1883 | D1857 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 1884 | D1858 | Design Number blank while TDW = 7.07 (>0, so it is compulsory) |
| 1885 | D1859 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1886 | D1860 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 1887 | D1861 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 1888 | D1862 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 1889 | D1863 | Design Number blank while TDW = 7.11 (>0, so it is compulsory) |
| 1890 | D1864 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 1891 | D1865 | Design Number blank while TDW = 7.22 (>0, so it is compulsory) |
| 1892 | D1866 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 1893 | D1867 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 1894 | D1868 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1895 | D1869 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 1896 | D1870 | Design Number blank while TDW = 5.07 (>0, so it is compulsory) |
| 1897 | D1871 | Design Number blank while TDW = 7.11 (>0, so it is compulsory) |
| 1898 | D1872 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 1899 | D1873 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1900 | D1874 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 1901 | D1875 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1902 | D1876 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1903 | D1877 | Design Number blank while TDW = 7.17 (>0, so it is compulsory) |
| 1904 | D1878 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 1905 | D1879 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 1906 | D1880 | Design Number blank while TDW = 5.09 (>0, so it is compulsory) |
| 1907 | D1881 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 1908 | D1882 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 1909 | D1883 | Design Number blank while TDW = 7.24 (>0, so it is compulsory) |
| 1910 | D1884 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1911 | D1885 | Design Number blank while TDW = 7.11 (>0, so it is compulsory) |
| 1912 | D1886 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 1913 | D1887 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 1914 | D1888 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 1915 | D1889 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 1916 | D1890 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 1917 | D1891 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 1918 | D1892 | Design Number blank while TDW = 7.03 (>0, so it is compulsory) |
| 1919 | D1893 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1920 | D1894 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 1921 | D1895 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 1922 | D1896 | Design Number blank while TDW = 7.32 (>0, so it is compulsory) |
| 1923 | D1897 | Design Number blank while TDW = 7.35 (>0, so it is compulsory) |
| 1924 | D1898 | Design Number blank while TDW = 7.14 (>0, so it is compulsory) |
| 1925 | D1899 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 1926 | D1900 | Design Number blank while TDW = 3.22 (>0, so it is compulsory) |
| 1927 | D1901 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 1928 | D1902 | Design Number blank while TDW = 3.22 (>0, so it is compulsory) |
| 1929 | D1903 | Design Number blank while TDW = 3.26 (>0, so it is compulsory) |
| 1930 | D1904 | Design Number blank while TDW = 3.18 (>0, so it is compulsory) |
| 1931 | D1905 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 1932 | D1906 | Design Number blank while TDW = 3.28 (>0, so it is compulsory) |
| 1933 | D1907 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1934 | D1908 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 1935 | D1909 | Design Number blank while TDW = 3.19 (>0, so it is compulsory) |
| 1936 | D1910 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 1937 | D1911 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 1938 | D1912 | Design Number blank while TDW = 3.26 (>0, so it is compulsory) |
| 1939 | D1913 | Design Number blank while TDW = 3.29 (>0, so it is compulsory) |
| 1940 | D1914 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 1941 | D1915 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1942 | D1916 | Design Number blank while TDW = 3.18 (>0, so it is compulsory) |
| 1943 | D1917 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 1944 | D1918 | Design Number blank while TDW = 3.36 (>0, so it is compulsory) |
| 1945 | D1919 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 1946 | D1920 | Design Number blank while TDW = 3.36 (>0, so it is compulsory) |
| 1947 | D1921 | Design Number blank while TDW = 3.36 (>0, so it is compulsory) |
| 1948 | D1922 | Design Number blank while TDW = 3.37 (>0, so it is compulsory) |
| 1949 | D1923 | Design Number blank while TDW = 3.16 (>0, so it is compulsory) |
| 1950 | D1924 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 1951 | D1925 | Design Number blank while TDW = 3.23 (>0, so it is compulsory) |
| 1952 | D1926 | Design Number blank while TDW = 3.38 (>0, so it is compulsory) |
| 1953 | D1927 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 1954 | D1928 | Design Number blank while TDW = 3.29 (>0, so it is compulsory) |
| 1955 | D1929 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 1956 | D1930 | Design Number blank while TDW = 3.26 (>0, so it is compulsory) |
| 1957 | D1931 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1958 | D1932 | Design Number blank while TDW = 3.35 (>0, so it is compulsory) |
| 1959 | D1933 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 1960 | D1934 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 1961 | D1935 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 1962 | D1936 | Design Number blank while TDW = 3.35 (>0, so it is compulsory) |
| 1963 | D1937 | Design Number blank while TDW = 3.2 (>0, so it is compulsory) |
| 1964 | D1938 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 1965 | D1939 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 1966 | D1940 | Design Number blank while TDW = 3.18 (>0, so it is compulsory) |
| 1967 | D1941 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1968 | D1942 | Design Number blank while TDW = 3.35 (>0, so it is compulsory) |
| 1969 | D1943 | Design Number blank while TDW = 3.19 (>0, so it is compulsory) |
| 1970 | D1944 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 1971 | D1945 | Design Number blank while TDW = 3.22 (>0, so it is compulsory) |
| 1972 | D1946 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 1973 | D1947 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 1974 | D1948 | Design Number blank while TDW = 3.22 (>0, so it is compulsory) |
| 1975 | D1949 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1976 | D1950 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1977 | D1951 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 1978 | D1952 | Design Number blank while TDW = 3.26 (>0, so it is compulsory) |
| 1979 | D1953 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 1980 | D1954 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 1981 | D1955 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 1982 | D1956 | Design Number blank while TDW = 3.23 (>0, so it is compulsory) |
| 1983 | D1957 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 1984 | D1958 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 1985 | D1959 | Design Number blank while TDW = 10.46 (>0, so it is compulsory) |
| 1986 | D1960 | Design Number blank while TDW = 10.45 (>0, so it is compulsory) |
| 1987 | D1961 | Design Number blank while TDW = 10.44 (>0, so it is compulsory) |
| 1988 | D1962 | Design Number blank while TDW = 10.37 (>0, so it is compulsory) |
| 1989 | D1963 | Design Number blank while TDW = 10.5 (>0, so it is compulsory) |
| 1990 | D1964 | Design Number blank while TDW = 10.58 (>0, so it is compulsory) |
| 1991 | D1965 | Design Number blank while TDW = 10.47 (>0, so it is compulsory) |
| 1992 | D1966 | Design Number blank while TDW = 10.42 (>0, so it is compulsory) |
| 1993 | D1967 | Design Number blank while TDW = 10.64 (>0, so it is compulsory) |
| 1994 | D1968 | Design Number blank while TDW = 14.77 (>0, so it is compulsory) |
| 1995 | D1969 | Design Number blank while TDW = 14.08 (>0, so it is compulsory) |
| 1996 | D1970 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 1997 | D1971 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1998 | D1972 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 1999 | D1973 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2000 | D1974 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2001 | D1975 | Design Number blank while TDW = 3.2 (>0, so it is compulsory) |
| 2002 | D1976 | Design Number blank while TDW = 3.2 (>0, so it is compulsory) |
| 2003 | D1977 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 2004 | D1978 | Design Number blank while TDW = 10.59 (>0, so it is compulsory) |
| 2005 | D1979 | Design Number blank while TDW = 10.53 (>0, so it is compulsory) |
| 2006 | D1980 | Design Number blank while TDW = 10.64 (>0, so it is compulsory) |
| 2007 | D1981 | Design Number blank while TDW = 10.59 (>0, so it is compulsory) |
| 2008 | D1982 | Design Number blank while TDW = 10.52 (>0, so it is compulsory) |
| 2009 | D1983 | Design Number blank while TDW = 10.64 (>0, so it is compulsory) |
| 2010 | D1984 | Design Number blank while TDW = 10.58 (>0, so it is compulsory) |
| 2011 | D1985 | Design Number blank while TDW = 10.47 (>0, so it is compulsory) |
| 2012 | D1986 | Design Number blank while TDW = 10.52 (>0, so it is compulsory) |
| 2013 | D1987 | Design Number blank while TDW = 7.31 (>0, so it is compulsory) |
| 2014 | D1988 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 2015 | D1989 | Design Number blank while TDW = 7.23 (>0, so it is compulsory) |
| 2016 | D1990 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 2017 | D1991 | Design Number blank while TDW = 7.24 (>0, so it is compulsory) |
| 2018 | D1992 | Design Number blank while TDW = 7.26 (>0, so it is compulsory) |
| 2019 | D1993 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 2020 | D1994 | Design Number blank while TDW = 7.26 (>0, so it is compulsory) |
| 2021 | D1995 | Design Number blank while TDW = 1.65 (>0, so it is compulsory) |
| 2022 | D1996 | Design Number blank while TDW = 0.8 (>0, so it is compulsory) |
| 2023 | D1997 | Design Number blank while TDW = 1.17 (>0, so it is compulsory) |
| 2024 | D1998 | Design Number blank while TDW = 10.38 (>0, so it is compulsory) |
| 2025 | D1999 | Design Number blank while TDW = 5.19 (>0, so it is compulsory) |
| 2026 | D2000 | Design Number blank while TDW = 3.267 (>0, so it is compulsory) |
| 2027 | D2001 | Design Number blank while TDW = 6.94 (>0, so it is compulsory) |
| 2028 | D2002 | Design Number blank while TDW = 10.63 (>0, so it is compulsory) |
| 2029 | D2003 | Design Number blank while TDW = 10.52 (>0, so it is compulsory) |
| 2030 | D2004 | Design Number blank while TDW = 10.69 (>0, so it is compulsory) |
| 2031 | D2005 | Design Number blank while TDW = 10.61 (>0, so it is compulsory) |
| 2032 | D2006 | Design Number blank while TDW = 10.64 (>0, so it is compulsory) |
| 2033 | D2007 | Design Number blank while TDW = 10.56 (>0, so it is compulsory) |
| 2034 | D2008 | Design Number blank while TDW = 10.62 (>0, so it is compulsory) |
| 2035 | D2009 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2036 | D2010 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2037 | D2011 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2038 | D2012 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 2039 | D2013 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2040 | D2014 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2041 | D2015 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2042 | D2016 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2043 | D2017 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2044 | D2018 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 2045 | D2019 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2045 | I2019 | Net 5.374 exceeds gross 4.246 while TDW = 4.98. With diamonds set, net must be less than gross |
| 2046 | D2020 | Design Number blank while TDW = 5.06 (>0, so it is compulsory) |
| 2047 | D2021 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2048 | D2022 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 2049 | D2023 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2050 | D2024 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 2051 | D2025 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2052 | D2026 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2053 | D2027 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2054 | D2028 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2055 | D2029 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2056 | D2030 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2057 | D2031 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2058 | D2032 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2059 | D2033 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 2060 | D2034 | Design Number blank while TDW = 5.06 (>0, so it is compulsory) |
| 2061 | D2035 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2062 | D2036 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2063 | D2037 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2064 | D2038 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2065 | D2039 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 2066 | D2040 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 2067 | D2041 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 2068 | D2042 | Design Number blank while TDW = 7.28 (>0, so it is compulsory) |
| 2069 | D2043 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 2070 | D2044 | Design Number blank while TDW = 7.1 (>0, so it is compulsory) |
| 2071 | D2045 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 2072 | D2046 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 2073 | D2047 | Design Number blank while TDW = 7.19 (>0, so it is compulsory) |
| 2074 | D2048 | Design Number blank while TDW = 7.12 (>0, so it is compulsory) |
| 2075 | D2049 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 2076 | D2050 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 2077 | D2051 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| 2078 | D2052 | Design Number blank while TDW = 7.27 (>0, so it is compulsory) |
| 2079 | D2053 | Design Number blank while TDW = 6.99 (>0, so it is compulsory) |
| 2080 | D2054 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 2081 | D2055 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2082 | D2056 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 2083 | D2057 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2084 | D2058 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2085 | D2059 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2086 | D2060 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2087 | D2061 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2088 | D2062 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2089 | D2063 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2090 | D2064 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2091 | D2065 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2092 | D2066 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 2093 | D2067 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2094 | D2068 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2095 | D2069 | Design Number blank while TDW = 5.06 (>0, so it is compulsory) |
| 2096 | D2070 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2097 | D2071 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2098 | D2072 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2099 | D2073 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 2100 | D2074 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 2101 | D2075 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 2102 | D2076 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2103 | D2077 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2104 | D2078 | Design Number blank while TDW = 5.34 (>0, so it is compulsory) |
| 2105 | D2079 | Design Number blank while TDW = 5.32 (>0, so it is compulsory) |
| 2106 | D2080 | Design Number blank while TDW = 5.37 (>0, so it is compulsory) |
| 2107 | D2081 | Design Number blank while TDW = 3.15 (>0, so it is compulsory) |
| 2108 | D2082 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 2109 | D2083 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 2110 | D2084 | Design Number blank while TDW = 3.29 (>0, so it is compulsory) |
| 2111 | D2085 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 2112 | D2086 | Design Number blank while TDW = 3.35 (>0, so it is compulsory) |
| 2113 | D2087 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 2114 | D2088 | Design Number blank while TDW = 3.38 (>0, so it is compulsory) |
| 2115 | D2089 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2116 | D2090 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 2117 | D2091 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2118 | D2092 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2119 | D2093 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2120 | D2094 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2121 | D2095 | Design Number blank while TDW = 3.29 (>0, so it is compulsory) |
| 2122 | D2096 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2123 | D2097 | Design Number blank while TDW = 3.18 (>0, so it is compulsory) |
| 2124 | D2098 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 2125 | D2099 | Design Number blank while TDW = 3.37 (>0, so it is compulsory) |
| 2126 | D2100 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 2127 | D2101 | Design Number blank while TDW = 3.37 (>0, so it is compulsory) |
| 2128 | D2102 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2129 | D2103 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 2130 | D2104 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 2131 | D2105 | Design Number blank while TDW = 3.36 (>0, so it is compulsory) |
| 2132 | D2106 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 2133 | D2107 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2134 | D2108 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 2135 | D2109 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2136 | D2110 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 2137 | D2111 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2138 | D2112 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2139 | D2113 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2140 | D2114 | Design Number blank while TDW = 3.26 (>0, so it is compulsory) |
| 2141 | D2115 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 2142 | D2116 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 2143 | D2117 | Design Number blank while TDW = 3.69 (>0, so it is compulsory) |
| 2144 | D2118 | Design Number blank while TDW = 3.1 (>0, so it is compulsory) |
| 2145 | D2119 | Design Number blank while TDW = 3.39 (>0, so it is compulsory) |
| 2146 | D2120 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2147 | D2121 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2148 | D2122 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2149 | D2123 | Design Number blank while TDW = 3.38 (>0, so it is compulsory) |
| 2150 | D2124 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2151 | D2125 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2152 | D2126 | Design Number blank while TDW = 4.9 (>0, so it is compulsory) |
| 2153 | D2127 | Design Number blank while TDW = 4.9 (>0, so it is compulsory) |
| 2154 | D2128 | Design Number blank while TDW = 4.91 (>0, so it is compulsory) |
| 2155 | D2129 | Design Number blank while TDW = 4.86 (>0, so it is compulsory) |
| 2156 | D2130 | Design Number blank while TDW = 4.92 (>0, so it is compulsory) |
| 2157 | D2131 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2158 | D2132 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 2159 | D2133 | Design Number blank while TDW = 4.91 (>0, so it is compulsory) |
| 2160 | D2134 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2161 | D2135 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2162 | D2136 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2163 | D2137 | Design Number blank while TDW = 5.06 (>0, so it is compulsory) |
| 2164 | D2138 | Design Number blank while TDW = 4.87 (>0, so it is compulsory) |
| 2165 | D2139 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2166 | D2140 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2167 | D2141 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 2168 | D2142 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2169 | D2143 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2170 | D2144 | Design Number blank while TDW = 4.92 (>0, so it is compulsory) |
| 2171 | D2145 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2172 | D2146 | Design Number blank while TDW = 5.98 (>0, so it is compulsory) |
| 2173 | D2147 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2174 | D2148 | Design Number blank while TDW = 5.38 (>0, so it is compulsory) |
| 2175 | D2149 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2176 | D2150 | Design Number blank while TDW = 4.85 (>0, so it is compulsory) |
| 2177 | D2151 | Design Number blank while TDW = 4.88 (>0, so it is compulsory) |
| 2178 | D2152 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2179 | D2153 | Design Number blank while TDW = 4.85 (>0, so it is compulsory) |
| 2180 | D2154 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2181 | D2155 | Design Number blank while TDW = 4.89 (>0, so it is compulsory) |
| 2182 | D2156 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2183 | D2157 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2184 | D2158 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2185 | D2159 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2186 | D2160 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2187 | D2161 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2188 | D2162 | Design Number blank while TDW = 4.89 (>0, so it is compulsory) |
| 2189 | D2163 | Design Number blank while TDW = 4.86 (>0, so it is compulsory) |
| 2190 | D2164 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2191 | D2165 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 2192 | D2166 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2193 | D2167 | Design Number blank while TDW = 5.03 (>0, so it is compulsory) |
| 2194 | D2168 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2195 | D2169 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2196 | D2170 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2197 | D2171 | Design Number blank while TDW = 5.1 (>0, so it is compulsory) |
| 2198 | D2172 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 2199 | D2173 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 2200 | D2174 | Design Number blank while TDW = 4.67 (>0, so it is compulsory) |
| 2201 | D2175 | Design Number blank while TDW = 10.24 (>0, so it is compulsory) |
| 2202 | D2176 | Design Number blank while TDW = 10.32 (>0, so it is compulsory) |
| 2203 | D2177 | Design Number blank while TDW = 10.33 (>0, so it is compulsory) |
| 2204 | D2178 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 2205 | D2179 | Design Number blank while TDW = 10.32 (>0, so it is compulsory) |
| 2206 | D2180 | Design Number blank while TDW = 3.24 (>0, so it is compulsory) |
| 2207 | D2181 | Design Number blank while TDW = 3.29 (>0, so it is compulsory) |
| 2208 | D2182 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2209 | D2183 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2210 | D2184 | Design Number blank while TDW = 3.27 (>0, so it is compulsory) |
| 2211 | D2185 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2212 | D2186 | Design Number blank while TDW = 3.21 (>0, so it is compulsory) |
| 2213 | D2187 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2214 | D2188 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2215 | D2189 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 2216 | D2190 | Design Number blank while TDW = 3.18 (>0, so it is compulsory) |
| 2217 | D2191 | Design Number blank while TDW = 3.34 (>0, so it is compulsory) |
| 2218 | D2192 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2219 | D2193 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2220 | D2194 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2221 | D2195 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2222 | D2196 | Design Number blank while TDW = 3.22 (>0, so it is compulsory) |
| 2223 | D2197 | Design Number blank while TDW = 3.3 (>0, so it is compulsory) |
| 2224 | D2198 | Design Number blank while TDW = 3.17 (>0, so it is compulsory) |
| 2225 | D2199 | Design Number blank while TDW = 3.33 (>0, so it is compulsory) |
| 2226 | D2200 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2227 | D2201 | Design Number blank while TDW = 4.89 (>0, so it is compulsory) |
| 2228 | D2202 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2229 | D2203 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 2230 | D2204 | Design Number blank while TDW = 5.04 (>0, so it is compulsory) |
| 2231 | D2205 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2232 | D2206 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2233 | D2207 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2234 | D2208 | Design Number blank while TDW = 4.98 (>0, so it is compulsory) |
| 2235 | D2209 | Design Number blank while TDW = 3.23 (>0, so it is compulsory) |
| 2236 | D2210 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2237 | D2211 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 2238 | D2212 | Design Number blank while TDW = 4.96 (>0, so it is compulsory) |
| 2239 | D2213 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2240 | D2214 | Design Number blank while TDW = 4.9 (>0, so it is compulsory) |
| 2241 | D2215 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2242 | D2216 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2243 | D2217 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2244 | D2218 | Design Number blank while TDW = 3.25 (>0, so it is compulsory) |
| 2245 | D2219 | Design Number blank while TDW = 10.64 (>0, so it is compulsory) |
| 2246 | D2220 | Design Number blank while TDW = 10.62 (>0, so it is compulsory) |
| 2247 | D2221 | Design Number blank while TDW = 10.58 (>0, so it is compulsory) |
| 2248 | D2222 | Design Number blank while TDW = 10.66 (>0, so it is compulsory) |
| 2249 | D2223 | Design Number blank while TDW = 10.51 (>0, so it is compulsory) |
| 2250 | D2224 | Design Number blank while TDW = 10.59 (>0, so it is compulsory) |
| 2251 | D2225 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2252 | D2226 | Design Number blank while TDW = 16.11 (>0, so it is compulsory) |
| 1691 | D2227 | Design Number blank while TDW = 2.84 (>0, so it is compulsory) |
| 1692 | D2228 | Design Number blank while TDW = 6.58 (>0, so it is compulsory) |
| 1693 | D2229 | Design Number blank while TDW = 10.1 (>0, so it is compulsory) |
| 1694 | D2230 | Design Number blank while TDW = 16.95 (>0, so it is compulsory) |
| 1695 | D2231 | Design Number blank while TDW = 11.13 (>0, so it is compulsory) |
| 1696 | D2232 | Design Number blank while TDW = 0.92 (>0, so it is compulsory) |
| 1697 | D2233 | Design Number blank while TDW = 1.02 (>0, so it is compulsory) |
| 1698 | D2234 | Design Number blank while TDW = 0.78 (>0, so it is compulsory) |
| 1699 | D2235 | Design Number blank while TDW = 0.8 (>0, so it is compulsory) |
| 1700 | D2236 | Design Number blank while TDW = 0.39 (>0, so it is compulsory) |
| 1701 | D2237 | Design Number blank while TDW = 0.72 (>0, so it is compulsory) |
| 1702 | D2238 | Design Number blank while TDW = 2.91 (>0, so it is compulsory) |
| 1703 | D2239 | Design Number blank while TDW = 1.4 (>0, so it is compulsory) |
| 1704 | D2240 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 1705 | D2241 | Design Number blank while TDW = 0.62 (>0, so it is compulsory) |
| 1706 | D2242 | Design Number blank while TDW = 2.5 (>0, so it is compulsory) |
| 1707 | D2243 | Design Number blank while TDW = 61.389 (>0, so it is compulsory) |
| 1708 | D2244 | Design Number blank while TDW = 1.31 (>0, so it is compulsory) |
| 1709 | D2245 | Design Number blank while TDW = 13.78 (>0, so it is compulsory) |
| 1710 | D2246 | Design Number blank while TDW = 9.1 (>0, so it is compulsory) |
| 1711 | D2247 | Design Number blank while TDW = 39.88 (>0, so it is compulsory) |
| 1712 | D2248 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 1713 | A2249 | Row has a Sr number but is otherwise empty (design, location, gold, gross, net, party all blank) |
| 2253 | D2250 | Design Number blank while TDW = 11.14 (>0, so it is compulsory) |
| 2254 | D2251 | Design Number blank while TDW = 2.77 (>0, so it is compulsory) |
| 2255 | D2252 | Design Number blank while TDW = 10.29 (>0, so it is compulsory) |
| 2256 | D2253 | Design Number blank while TDW = 5.55 (>0, so it is compulsory) |
| 2257 | D2254 | Design Number blank while TDW = 13.18 (>0, so it is compulsory) |
| 2258 | D2255 | Design Number blank while TDW = 4.82 (>0, so it is compulsory) |
| 2259 | D2256 | Design Number blank while TDW = 67.37 (>0, so it is compulsory) |
| 2260 | D2257 | Design Number blank while TDW = 5.91 (>0, so it is compulsory) |
| 2261 | D2258 | Design Number blank while TDW = 32.43 (>0, so it is compulsory) |
| 2262 | D2259 | Design Number blank while TDW = 11.43 (>0, so it is compulsory) |
| 2263 | D2260 | Design Number blank while TDW = 32.63 (>0, so it is compulsory) |
| 2264 | D2261 | Design Number blank while TDW = 7.41 (>0, so it is compulsory) |
| 2265 | D2262 | Design Number blank while TDW = 43.65 (>0, so it is compulsory) |
| 2266 | D2263 | Design Number blank while TDW = 19.2 (>0, so it is compulsory) |
| 2267 | D2264 | Design Number blank while TDW = 31.02 (>0, so it is compulsory) |
| 2268 | D2265 | Design Number blank while TDW = 7.83 (>0, so it is compulsory) |
| 2269 | D2266 | Design Number blank while TDW = 23.59 (>0, so it is compulsory) |
| 2270 | D2267 | Design Number blank while TDW = 8.25 (>0, so it is compulsory) |
| 2271 | D2268 | Design Number blank while TDW = 24.83 (>0, so it is compulsory) |
| 2272 | D2269 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 2273 | D2270 | Design Number blank while TDW = 65.43 (>0, so it is compulsory) |
| 2274 | D2271 | Design Number blank while TDW = 13.11 (>0, so it is compulsory) |
| 2275 | D2272 | Design Number blank while TDW = 30.28 (>0, so it is compulsory) |
| 2276 | D2273 | Design Number blank while TDW = 10.03 (>0, so it is compulsory) |
| 2277 | D2274 | Design Number blank while TDW = 10.2 (>0, so it is compulsory) |
| 2278 | D2275 | Design Number blank while TDW = 3.16 (>0, so it is compulsory) |
| 2279 | D2276 | Design Number blank while TDW = 133.84 (>0, so it is compulsory) |
| 2280 | D2277 | Design Number blank while TDW = 7.65 (>0, so it is compulsory) |
| 2281 | D2278 | Design Number blank while TDW = 35.55 (>0, so it is compulsory) |
| 2282 | D2279 | Design Number blank while TDW = 12.4 (>0, so it is compulsory) |
| 2283 | D2280 | Design Number blank while TDW = 81.53 (>0, so it is compulsory) |
| 2284 | D2281 | Design Number blank while TDW = 20.85 (>0, so it is compulsory) |
| 2285 | D2282 | Design Number blank while TDW = 11.21 (>0, so it is compulsory) |
| 2286 | D2283 | Design Number blank while TDW = 14.29 (>0, so it is compulsory) |
| 2286 | I2283 | Net 59.5 exceeds gross 14.718 while TDW = 14.29. With diamonds set, net must be less than gross |
| 2287 | D2284 | Design Number blank while TDW = 36.14 (>0, so it is compulsory) |
| 2288 | D2285 | Design Number blank while TDW = 13.15 (>0, so it is compulsory) |
| 2289 | D2286 | Design Number blank while TDW = 37.89 (>0, so it is compulsory) |
| 2290 | D2287 | Design Number blank while TDW = 9.02 (>0, so it is compulsory) |
| 2291 | D2288 | Design Number blank while TDW = 107.1 (>0, so it is compulsory) |
| 2292 | D2289 | Design Number blank while TDW = 41.79 (>0, so it is compulsory) |
| 2293 | D2290 | Design Number blank while TDW = 6.72 (>0, so it is compulsory) |
| 2294 | D2291 | Design Number blank while TDW = 6.8 (>0, so it is compulsory) |
| 2295 | D2292 | Design Number blank while TDW = 4.97 (>0, so it is compulsory) |
| 2296 | D2293 | Design Number blank while TDW = 4.94 (>0, so it is compulsory) |
| 2297 | D2294 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 2298 | D2295 | Design Number blank while TDW = 5.01 (>0, so it is compulsory) |
| 2299 | D2296 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| 2300 | D2297 | Design Number blank while TDW = 7.18 (>0, so it is compulsory) |
| 2301 | D2298 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 2302 | D2299 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 2303 | D2300 | Design Number blank while TDW = 5.18 (>0, so it is compulsory) |
| 2304 | D2301 | Design Number blank while TDW = 6.08 (>0, so it is compulsory) |
| 2305 | D2302 | Design Number blank while TDW = 5.9 (>0, so it is compulsory) |
| 2306 | D2303 | Design Number blank while TDW = 5.9 (>0, so it is compulsory) |
| 2307 | D2304 | Design Number blank while TDW = 5.9 (>0, so it is compulsory) |
| 2308 | D2305 | Design Number blank while TDW = 5.81 (>0, so it is compulsory) |
| 2309 | D2306 | Design Number blank while TDW = 5.81 (>0, so it is compulsory) |
| 2310 | D2307 | Design Number blank while TDW = 1.5 (>0, so it is compulsory) |
| 2311 | D2308 | Design Number blank while TDW = 4.22 (>0, so it is compulsory) |
| 2312 | D2309 | Design Number blank while TDW = 1.89 (>0, so it is compulsory) |
| 2313 | D2310 | Design Number blank while TDW = 1.51 (>0, so it is compulsory) |
| 2314 | D2311 | Design Number blank while TDW = 2.19 (>0, so it is compulsory) |
| 2315 | D2312 | Design Number blank while TDW = 0.62 (>0, so it is compulsory) |
| 2316 | D2313 | Design Number blank while TDW = 1.93 (>0, so it is compulsory) |
| 2317 | D2314 | Design Number blank while TDW = 2.26 (>0, so it is compulsory) |
| 2318 | D2315 | Design Number blank while TDW = 2.11 (>0, so it is compulsory) |
| 2319 | D2316 | Design Number blank while TDW = 2.25 (>0, so it is compulsory) |
| 2320 | D2317 | Design Number blank while TDW = 2.07 (>0, so it is compulsory) |
| 2321 | D2318 | Design Number blank while TDW = 2.26 (>0, so it is compulsory) |
| 2322 | D2319 | Design Number blank while TDW = 7.66 (>0, so it is compulsory) |
| 2323 | D2320 | Design Number blank while TDW = 2.24 (>0, so it is compulsory) |
| 2324 | D2321 | Design Number blank while TDW = 2.27 (>0, so it is compulsory) |
| 2325 | D2322 | Design Number blank while TDW = 2.1 (>0, so it is compulsory) |
| 2326 | D2323 | Design Number blank while TDW = 6.87 (>0, so it is compulsory) |
| 2327 | D2324 | Design Number blank while TDW = 2.21 (>0, so it is compulsory) |
| 2328 | D2325 | Design Number blank while TDW = 0.59 (>0, so it is compulsory) |
| 2329 | D2326 | Design Number blank while TDW = 2.11 (>0, so it is compulsory) |
| 2330 | D2327 | Design Number blank while TDW = 1.29 (>0, so it is compulsory) |
| 2331 | D2328 | Design Number blank while TDW = 3.08 (>0, so it is compulsory) |
| 2332 | D2329 | Design Number blank while TDW = 2.02 (>0, so it is compulsory) |
| 2333 | D2330 | Design Number blank while TDW = 1.78 (>0, so it is compulsory) |
| 2334 | D2331 | Design Number blank while TDW = 1.91 (>0, so it is compulsory) |
| 2335 | D2332 | Design Number blank while TDW = 3.07 (>0, so it is compulsory) |
| 2336 | D2333 | Design Number blank while TDW = 2.28 (>0, so it is compulsory) |
| 2337 | D2334 | Design Number blank while TDW = 4.65 (>0, so it is compulsory) |
| 2338 | D2335 | Design Number blank while TDW = 2.12 (>0, so it is compulsory) |
| 2339 | D2336 | Design Number blank while TDW = 1.48 (>0, so it is compulsory) |
| 2340 | D2337 | Design Number blank while TDW = 1.28 (>0, so it is compulsory) |
| 2341 | D2338 | Design Number blank while TDW = 2.72 (>0, so it is compulsory) |
| 2342 | D2339 | Design Number blank while TDW = 4.62 (>0, so it is compulsory) |
| 2343 | D2340 | Design Number blank while TDW = 1.95 (>0, so it is compulsory) |
| 2344 | D2341 | Design Number blank while TDW = 2.9 (>0, so it is compulsory) |
| 2345 | D2342 | Design Number blank while TDW = 15.39 (>0, so it is compulsory) |
| 2346 | D2343 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| 2347 | D2344 | Design Number blank while TDW = 2.94 (>0, so it is compulsory) |
| 2348 | D2345 | Design Number blank while TDW = 14.6 (>0, so it is compulsory) |
| 2349 | D2346 | Design Number blank while TDW = 15.35 (>0, so it is compulsory) |
| 2350 | D2347 | Design Number blank while TDW = 10.13 (>0, so it is compulsory) |
| 2351 | D2348 | Design Number blank while TDW = 4.87 (>0, so it is compulsory) |
| 2352 | D2349 | Design Number blank while TDW = 2.85 (>0, so it is compulsory) |
| 2353 | D2350 | Design Number blank while TDW = 4.86 (>0, so it is compulsory) |
| 2354 | D2351 | Design Number blank while TDW = 10.09 (>0, so it is compulsory) |
| 2355 | D2352 | Design Number blank while TDW = 1.94 (>0, so it is compulsory) |
| 2356 | D2353 | Design Number blank while TDW = 6.76 (>0, so it is compulsory) |
| 2357 | D2354 | Design Number blank while TDW = 6.63 (>0, so it is compulsory) |
| 2358 | D2355 | Design Number blank while TDW = 23.57 (>0, so it is compulsory) |
| 2359 | D2356 | Design Number blank while TDW = 3.48 (>0, so it is compulsory) |
| 2360 | D2357 | Design Number blank while TDW = 3.46 (>0, so it is compulsory) |
| 2361 | D2358 | Design Number blank while TDW = 3.7 (>0, so it is compulsory) |
| 2362 | D2359 | Design Number blank while TDW = 5.15 (>0, so it is compulsory) |
| 2363 | D2360 | Design Number blank while TDW = 3.73 (>0, so it is compulsory) |
| 2364 | D2361 | Design Number blank while TDW = 5.37 (>0, so it is compulsory) |
| 2365 | D2362 | Design Number blank while TDW = 5.46 (>0, so it is compulsory) |
| 2366 | D2363 | Design Number blank while TDW = 3.61 (>0, so it is compulsory) |
| 2367 | D2364 | Design Number blank while TDW = 3.41 (>0, so it is compulsory) |
| 2368 | D2365 | Design Number blank while TDW = 3.7 (>0, so it is compulsory) |
| 2369 | D2366 | Design Number blank while TDW = 3.52 (>0, so it is compulsory) |
| 2370 | D2367 | Design Number blank while TDW = 5.47 (>0, so it is compulsory) |
| 2371 | D2368 | Design Number blank while TDW = 3.48 (>0, so it is compulsory) |
| 2372 | D2369 | Design Number blank while TDW = 3.68 (>0, so it is compulsory) |
| 2373 | D2370 | Design Number blank while TDW = 7.53 (>0, so it is compulsory) |
| 2374 | D2371 | Design Number blank while TDW = 9.54 (>0, so it is compulsory) |
| 2375 | D2372 | Design Number blank while TDW = 8.86 (>0, so it is compulsory) |
| 2376 | D2373 | Design Number blank while TDW = 7.96 (>0, so it is compulsory) |
| 2377 | D2374 | Design Number blank while TDW = 12.72 (>0, so it is compulsory) |
| 2378 | D2375 | Design Number blank while TDW = 3.18 (>0, so it is compulsory) |
| 2379 | D2376 | Design Number blank while TDW = 2.29 (>0, so it is compulsory) |
| 2380 | D2377 | Design Number blank while TDW = 3.7 (>0, so it is compulsory) |
| 2381 | D2378 | Design Number blank while TDW = 3.44 (>0, so it is compulsory) |
| 2382 | D2379 | Design Number blank while TDW = 6.12 (>0, so it is compulsory) |
| 2383 | D2380 | Design Number blank while TDW = 6.08 (>0, so it is compulsory) |
| 2384 | D2381 | Design Number blank while TDW = 6.07 (>0, so it is compulsory) |
| 2385 | D2382 | Design Number blank while TDW = 10.56 (>0, so it is compulsory) |
| 2386 | D2383 | Design Number blank while TDW = 10.58 (>0, so it is compulsory) |
| 2387 | D2384 | Design Number blank while TDW = 10.6 (>0, so it is compulsory) |
| 2388 | D2385 | Design Number blank while TDW = 9.89 (>0, so it is compulsory) |
| 2389 | D2386 | Design Number blank while TDW = 10.61 (>0, so it is compulsory) |
| 2390 | D2387 | Design Number blank while TDW = 10.6 (>0, so it is compulsory) |
| 2391 | D2388 | Design Number blank while TDW = 10.59 (>0, so it is compulsory) |
| 2392 | D2389 | Design Number blank while TDW = 10.71 (>0, so it is compulsory) |
| 2393 | D2390 | Design Number blank while TDW = 10.65 (>0, so it is compulsory) |
| 2394 | D2391 | Design Number blank while TDW = 10.71 (>0, so it is compulsory) |
| 2395 | D2392 | Design Number blank while TDW = 10.72 (>0, so it is compulsory) |
| 2396 | D2393 | Design Number blank while TDW = 9.96 (>0, so it is compulsory) |
| 2397 | D2394 | Design Number blank while TDW = 9.93 (>0, so it is compulsory) |
| 2398 | D2395 | Design Number blank while TDW = 9.94 (>0, so it is compulsory) |
| 2399 | D2396 | Design Number blank while TDW = 9.8 (>0, so it is compulsory) |
| 2400 | D2397 | Design Number blank while TDW = 9.88 (>0, so it is compulsory) |
| 2401 | D2398 | Design Number blank while TDW = 9.81 (>0, so it is compulsory) |
| 2402 | D2399 | Design Number blank while TDW = 10.58 (>0, so it is compulsory) |
| 2403 | D2400 | Design Number blank while TDW = 9.86 (>0, so it is compulsory) |
| 2404 | D2401 | Design Number blank while TDW = 9.86 (>0, so it is compulsory) |
| 2405 | D2402 | Design Number blank while TDW = 9.9 (>0, so it is compulsory) |
| 2406 | D2403 | Design Number blank while TDW = 9.99 (>0, so it is compulsory) |
| 2407 | D2404 | Design Number blank while TDW = 9.85 (>0, so it is compulsory) |
| 2408 | D2405 | Design Number blank while TDW = 9.81 (>0, so it is compulsory) |
| 2409 | D2406 | Design Number blank while TDW = 9.84 (>0, so it is compulsory) |
| 2410 | D2407 | Design Number blank while TDW = 9.8 (>0, so it is compulsory) |
| 2411 | D2408 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 2412 | D2409 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 2413 | D2410 | Design Number blank while TDW = 7.05 (>0, so it is compulsory) |
| 2414 | D2411 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 2415 | D2412 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 2416 | D2413 | Design Number blank while TDW = 7.15 (>0, so it is compulsory) |
| 2417 | D2414 | Design Number blank while TDW = 28.82 (>0, so it is compulsory) |
| 2418 | D2415 | Design Number blank while TDW = 27.59 (>0, so it is compulsory) |
| 2419 | D2416 | Design Number blank while TDW = 23.68 (>0, so it is compulsory) |
| 2420 | D2417 | Design Number blank while TDW = 19.57 (>0, so it is compulsory) |
| 2421 | D2418 | Design Number blank while TDW = 11.04 (>0, so it is compulsory) |
| 2422 | D2419 | Design Number blank while TDW = 35.19 (>0, so it is compulsory) |
| 2423 | D2420 | Design Number blank while TDW = 29.98 (>0, so it is compulsory) |
| 2424 | D2421 | Design Number blank while TDW = 36.06 (>0, so it is compulsory) |
| 2425 | D2422 | Design Number blank while TDW = 9.84 (>0, so it is compulsory) |
| 2426 | D2423 | Design Number blank while TDW = 9.92 (>0, so it is compulsory) |
| 2427 | D2424 | Design Number blank while TDW = 10.01 (>0, so it is compulsory) |
| 2428 | D2425 | Design Number blank while TDW = 9.88 (>0, so it is compulsory) |
| 2429 | D2426 | Design Number blank while TDW = 3.32 (>0, so it is compulsory) |
| 2430 | D2427 | Design Number blank while TDW = 3.31 (>0, so it is compulsory) |
| 2431 | D2428 | Design Number blank while TDW = 26.37 (>0, so it is compulsory) |
| 2432 | D2429 | Design Number blank while TDW = 4.78 (>0, so it is compulsory) |
| 2433 | D2430 | Design Number blank while TDW = 1.92 (>0, so it is compulsory) |
| 2434 | D2431 | Design Number blank while TDW = 7.88 (>0, so it is compulsory) |
| 2435 | D2432 | Design Number blank while TDW = 7.64 (>0, so it is compulsory) |
| 2436 | D2433 | Design Number blank while TDW = 7.32 (>0, so it is compulsory) |
| 2437 | D2434 | Design Number blank while TDW = 1.94 (>0, so it is compulsory) |
| 2438 | D2435 | Design Number blank while TDW = 12.89 (>0, so it is compulsory) |
| 2439 | D2436 | Design Number blank while TDW = 4.84 (>0, so it is compulsory) |
| 2440 | D2437 | Design Number blank while TDW = 3.84 (>0, so it is compulsory) |
| 2441 | D2438 | Design Number blank while TDW = 13.24 (>0, so it is compulsory) |
| 2442 | D2439 | Design Number blank while TDW = 12.26 (>0, so it is compulsory) |
| 2443 | D2440 | Design Number blank while TDW = 8.09 (>0, so it is compulsory) |
| 2444 | D2441 | Design Number blank while TDW = 5.08 (>0, so it is compulsory) |
| 2445 | D2442 | Design Number blank while TDW = 13.14 (>0, so it is compulsory) |
| 2446 | D2443 | Design Number blank while TDW = 8.33 (>0, so it is compulsory) |
| 2447 | D2444 | Design Number blank while TDW = 5.15 (>0, so it is compulsory) |
| 2448 | D2445 | Design Number blank while TDW = 1.98 (>0, so it is compulsory) |
| 2449 | D2446 | Design Number blank while TDW = 13.1 (>0, so it is compulsory) |
| 2450 | D2447 | Design Number blank while TDW = 5.63 (>0, so it is compulsory) |
| 2451 | D2448 | Design Number blank while TDW = 5.46 (>0, so it is compulsory) |
| 2452 | D2449 | Design Number blank while TDW = 5.4 (>0, so it is compulsory) |
| 2453 | D2450 | Design Number blank while TDW = 2.67 (>0, so it is compulsory) |
| 2454 | D2451 | Design Number blank while TDW = 7.9 (>0, so it is compulsory) |
| 2455 | D2452 | Design Number blank while TDW = 2.12 (>0, so it is compulsory) |
| 2456 | D2453 | Design Number blank while TDW = 4.89 (>0, so it is compulsory) |
| 2457 | D2454 | Design Number blank while TDW = 3.88 (>0, so it is compulsory) |
| 2458 | D2455 | Design Number blank while TDW = 3.43 (>0, so it is compulsory) |
| 2459 | D2456 | Design Number blank while TDW = 3.41 (>0, so it is compulsory) |
| 2460 | D2457 | Design Number blank while TDW = 10.49 (>0, so it is compulsory) |
| 2461 | D2458 | Design Number blank while TDW = 12.74 (>0, so it is compulsory) |
| 2462 | D2459 | Design Number blank while TDW = 4.73 (>0, so it is compulsory) |
| 2463 | D2460 | Design Number blank while TDW = 4.85 (>0, so it is compulsory) |
| 2464 | D2461 | Design Number blank while TDW = 7.93 (>0, so it is compulsory) |
| 2465 | D2462 | Design Number blank while TDW = 2.29 (>0, so it is compulsory) |
| 2466 | D2463 | Design Number blank while TDW = 13.12 (>0, so it is compulsory) |
| 2467 | D2464 | Design Number blank while TDW = 3.65 (>0, so it is compulsory) |
| 2468 | D2465 | Design Number blank while TDW = 3.68 (>0, so it is compulsory) |
| 2469 | D2466 | Design Number blank while TDW = 2.24 (>0, so it is compulsory) |
| 2470 | D2467 | Design Number blank while TDW = 3.76 (>0, so it is compulsory) |
| 2471 | D2468 | Design Number blank while TDW = 9.81 (>0, so it is compulsory) |
| 2472 | D2469 | Design Number blank while TDW = 6.84 (>0, so it is compulsory) |
| 2473 | D2470 | Design Number blank while TDW = 4.13 (>0, so it is compulsory) |
| 2474 | D2471 | Design Number blank while TDW = 3.06 (>0, so it is compulsory) |
| 2475 | D2472 | Design Number blank while TDW = 5.54 (>0, so it is compulsory) |
| 2476 | D2473 | Design Number blank while TDW = 31.22 (>0, so it is compulsory) |
| 2477 | D2474 | Design Number blank while TDW = 7.16 (>0, so it is compulsory) |
| 2478 | D2475 | Design Number blank while TDW = 5.02 (>0, so it is compulsory) |
| 2479 | D2476 | Design Number blank while TDW = 7.08 (>0, so it is compulsory) |
| 2480 | D2477 | Design Number blank while TDW = 5.0 (>0, so it is compulsory) |
| 2481 | D2478 | Design Number blank while TDW = 4.93 (>0, so it is compulsory) |
| 2482 | D2479 | Design Number blank while TDW = 7.2 (>0, so it is compulsory) |
| 2483 | D2480 | Design Number blank while TDW = 7.21 (>0, so it is compulsory) |
| 2484 | D2481 | Design Number blank while TDW = 9.53 (>0, so it is compulsory) |
| 2485 | D2482 | Design Number blank while TDW = 7.26 (>0, so it is compulsory) |
| 2486 | D2483 | Design Number blank while TDW = 5.05 (>0, so it is compulsory) |
| 2487 | D2484 | Design Number blank while TDW = 7.31 (>0, so it is compulsory) |
| 2488 | D2485 | Design Number blank while TDW = 9.18 (>0, so it is compulsory) |
| 2489 | D2486 | Design Number blank while TDW = 9.67 (>0, so it is compulsory) |
| 2490 | D2487 | Design Number blank while TDW = 9.74 (>0, so it is compulsory) |
| 2491 | D2488 | Design Number blank while TDW = 9.67 (>0, so it is compulsory) |
| 2492 | D2489 | Design Number blank while TDW = 9.77 (>0, so it is compulsory) |
| 2493 | D2490 | Design Number blank while TDW = 9.59 (>0, so it is compulsory) |
| 2494 | D2491 | Design Number blank while TDW = 9.81 (>0, so it is compulsory) |
| 2495 | D2492 | Design Number blank while TDW = 9.75 (>0, so it is compulsory) |
| 2496 | D2493 | Design Number blank while TDW = 9.66 (>0, so it is compulsory) |
| 2497 | D2494 | Design Number blank while TDW = 9.7 (>0, so it is compulsory) |
| 2498 | D2495 | Design Number blank while TDW = 9.57 (>0, so it is compulsory) |
| 2499 | D2496 | Design Number blank while TDW = 9.55 (>0, so it is compulsory) |
| 2500 | D2497 | Design Number blank while TDW = 9.61 (>0, so it is compulsory) |
| A0001 | D2498 | Design Number blank while TDW = 9.7 (>0, so it is compulsory) |
| A0002 | D2499 | Design Number blank while TDW = 9.57 (>0, so it is compulsory) |
| A0003 | D2500 | Design Number blank while TDW = 9.61 (>0, so it is compulsory) |
| A0004 | D2501 | Design Number blank while TDW = 9.7 (>0, so it is compulsory) |
| A0005 | D2502 | Design Number blank while TDW = 9.71 (>0, so it is compulsory) |
| A0006 | D2503 | Design Number blank while TDW = 9.63 (>0, so it is compulsory) |
| A0007 | D2504 | Design Number blank while TDW = 9.64 (>0, so it is compulsory) |
| A0008 | D2505 | Design Number blank while TDW = 9.6 (>0, so it is compulsory) |
| A0009 | D2506 | Design Number blank while TDW = 9.79 (>0, so it is compulsory) |
| A0010 | D2507 | Design Number blank while TDW = 9.59 (>0, so it is compulsory) |
| A0011 | D2508 | Design Number blank while TDW = 9.69 (>0, so it is compulsory) |
| A0012 | D2509 | Design Number blank while TDW = 9.73 (>0, so it is compulsory) |
| A0013 | D2510 | Design Number blank while TDW = 9.63 (>0, so it is compulsory) |
| A0014 | D2511 | Design Number blank while TDW = 9.63 (>0, so it is compulsory) |
| A0015 | D2512 | Design Number blank while TDW = 9.75 (>0, so it is compulsory) |
| A0016 | D2513 | Design Number blank while TDW = 9.51 (>0, so it is compulsory) |
| A0017 | D2514 | Design Number blank while TDW = 9.68 (>0, so it is compulsory) |
| A0018 | D2515 | Design Number blank while TDW = 9.64 (>0, so it is compulsory) |
| A0019 | D2516 | Design Number blank while TDW = 9.64 (>0, so it is compulsory) |
| A0020 | D2517 | Design Number blank while TDW = 9.83 (>0, so it is compulsory) |
| A0021 | D2518 | Design Number blank while TDW = 9.75 (>0, so it is compulsory) |
| A0022 | D2519 | Design Number blank while TDW = 9.72 (>0, so it is compulsory) |
| A0023 | D2520 | Design Number blank while TDW = 9.65 (>0, so it is compulsory) |
| A0024 | D2521 | Design Number blank while TDW = 9.67 (>0, so it is compulsory) |
| A0025 | D2522 | Design Number blank while TDW = 9.63 (>0, so it is compulsory) |
| A0026 | D2523 | Design Number blank while TDW = 4.95 (>0, so it is compulsory) |
| A0027 | D2524 | Design Number blank while TDW = 9.64 (>0, so it is compulsory) |
| A0028 | D2525 | Design Number blank while TDW = 17.47 (>0, so it is compulsory) |
| A0029 | D2526 | Design Number blank while TDW = 2.78 (>0, so it is compulsory) |
| A0030 | D2527 | Design Number blank while TDW = 2.94 (>0, so it is compulsory) |
| A0031 | D2528 | Design Number blank while TDW = 1.97 (>0, so it is compulsory) |
| A0032 | D2529 | Design Number blank while TDW = 2.9 (>0, so it is compulsory) |
| A0033 | D2530 | Design Number blank while TDW = 4.62 (>0, so it is compulsory) |
| A0034 | D2531 | Design Number blank while TDW = 5.37 (>0, so it is compulsory) |
| A0035 | D2532 | Design Number blank while TDW = 7.47 (>0, so it is compulsory) |
| A0036 | D2533 | Design Number blank while TDW = 12.28 (>0, so it is compulsory) |
| A0037 | D2534 | Design Number blank while TDW = 4.99 (>0, so it is compulsory) |
| A0038 | D2535 | Design Number blank while TDW = 2.23 (>0, so it is compulsory) |
| A0039 | D2536 | Design Number blank while TDW = 11.77 (>0, so it is compulsory) |
| A0040 | D2537 | Design Number blank while TDW = 2.15 (>0, so it is compulsory) |
| A0041 | D2538 | Design Number blank while TDW = 2.06 (>0, so it is compulsory) |
| A0042 | D2539 | Design Number blank while TDW = 2.06 (>0, so it is compulsory) |
| A0043 | D2540 | Design Number blank while TDW = 2.05 (>0, so it is compulsory) |
| A0044 | D2541 | Design Number blank while TDW = 2.09 (>0, so it is compulsory) |
| A0045 | D2542 | Design Number blank while TDW = 2.14 (>0, so it is compulsory) |
| A0046 | D2543 | Design Number blank while TDW = 2.04 (>0, so it is compulsory) |
| A0047 | D2544 | Design Number blank while TDW = 2.13 (>0, so it is compulsory) |
| A0048 | D2545 | Design Number blank while TDW = 2.14 (>0, so it is compulsory) |
| A0049 | D2546 | Design Number blank while TDW = 2.12 (>0, so it is compulsory) |
| A0050 | D2547 | Design Number blank while TDW = 2.11 (>0, so it is compulsory) |
| A0051 | D2548 | Design Number blank while TDW = 2.14 (>0, so it is compulsory) |
| A0052 | D2549 | Design Number blank while TDW = 2.09 (>0, so it is compulsory) |
| A0053 | D2550 | Design Number blank while TDW = 0.97 (>0, so it is compulsory) |
| A0054 | D2551 | Design Number blank while TDW = 0.97 (>0, so it is compulsory) |
| A0055 | D2552 | Design Number blank while TDW = 0.95 (>0, so it is compulsory) |
| A0056 | D2553 | Design Number blank while TDW = 0.97 (>0, so it is compulsory) |
| A0057 | D2554 | Design Number blank while TDW = 0.96 (>0, so it is compulsory) |
| A0058 | D2555 | Design Number blank while TDW = 0.96 (>0, so it is compulsory) |
| A0059 | D2556 | Design Number blank while TDW = 0.98 (>0, so it is compulsory) |
| A0153 | D2650 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| A0154 | D2651 | Design Number blank while TDW = 7.02 (>0, so it is compulsory) |
| A0155 | D2652 | Design Number blank while TDW = 7.0 (>0, so it is compulsory) |
| A0156 | D2653 | Design Number blank while TDW = 7.01 (>0, so it is compulsory) |
| A0157 | D2654 | Design Number blank while TDW = 6.96 (>0, so it is compulsory) |
| A0158 | D2655 | Design Number blank while TDW = 6.94 (>0, so it is compulsory) |
| A0159 | D2656 | Design Number blank while TDW = 6.96 (>0, so it is compulsory) |
| A0160 | D2657 | Design Number blank while TDW = 7.03 (>0, so it is compulsory) |
| A0161 | D2658 | Design Number blank while TDW = 7.03 (>0, so it is compulsory) |
| A0162 | D2659 | Design Number blank while TDW = 11.07 (>0, so it is compulsory) |
| A0163 | D2660 | Design Number blank while TDW = 45.29 (>0, so it is compulsory) |
| A0164 | D2661 | Design Number blank while TDW = 6.71 (>0, so it is compulsory) |
| A0165 | D2662 | Design Number blank while TDW = 2.66 (>0, so it is compulsory) |
| A0166 | D2663 | Design Number blank while TDW = 1.88 (>0, so it is compulsory) |
| A0167 | D2664 | Design Number blank while TDW = 4.86 (>0, so it is compulsory) |
| A0168 | D2665 | Design Number blank while TDW = 3.02 (>0, so it is compulsory) |
| A0169 | D2666 | Design Number blank while TDW = 7.13 (>0, so it is compulsory) |
| A0170 | D2667 | Design Number blank while TDW = 11.55 (>0, so it is compulsory) |
| A0171 | D2668 | Design Number blank while TDW = 6.94 (>0, so it is compulsory) |
| A0172 | D2669 | Design Number blank while TDW = 6.76 (>0, so it is compulsory) |
| A0287 | G2784 | Ring size 'US 7' has a space — expected 'US7' |
| A0288 | G2785 | Ring size 'US 7' has a space — expected 'US7' |
| A0310 | D2807 | Design Number blank while TDW = 18.77 (>0, so it is compulsory) |
| A0311 | D2808 | Design Number blank while TDW = 9.5 (>0, so it is compulsory) |
| A0312 | D2809 | Design Number blank while TDW = 210.73 (>0, so it is compulsory) |
| A0313 | D2810 | Design Number blank while TDW = 9.27 (>0, so it is compulsory) |
| A0314 | D2811 | Design Number blank while TDW = 19.18 (>0, so it is compulsory) |
| A0315 | D2812 | Design Number blank while TDW = 37.02 (>0, so it is compulsory) |
| A0316 | D2813 | Design Number blank while TDW = 95.34 (>0, so it is compulsory) |
| A0339 | D2836 | Design Number blank while TDW = 10.96 (>0, so it is compulsory) |
| A0340 | D2837 | Design Number blank while TDW = 30.63 (>0, so it is compulsory) |
| A0421 | D2918 | Design Number blank while TDW = 9.89 (>0, so it is compulsory) |
| A0474 | G2971 | Ring size 'US 4' has a space — expected 'US4' |
| A0574 | D3071 | Design Number blank while TDW = 5.94 (>0, so it is compulsory) |
| A0620 | G3117 | Ring size 'US 7' has a space — expected 'US7' |
| A0621 | G3118 | Ring size 'US 7' has a space — expected 'US7' |
| A0622 | G3119 | Ring size 'US 7' has a space — expected 'US7' |
| A0623 | G3120 | Ring size 'US 7' has a space — expected 'US7' |
| A0695 | R3192 | Product Code blank while TDW = 5.52 |
| A0697 | R3194 | Product Code blank while TDW = 3.55 |
| A0886 | G3383 | Ring size 'US 7' has a space — expected 'US7' |
| A0887 | G3384 | Ring size 'US 7' has a space — expected 'US7' |
| A0888 | G3385 | Ring size 'US 7' has a space — expected 'US7' |
| A0911 | G3408 | Ring size 'US 7' has a space — expected 'US7' |
| A1031 | G3528 | Ring size 'US 7' has a space — expected 'US7' |
| A1032 | G3529 | Ring size 'US 7' has a space — expected 'US7' |
| A1033 | G3530 | Ring size 'US 7' has a space — expected 'US7' |
| A1034 | G3531 | Ring size 'US 7' has a space — expected 'US7' |
| A1035 | G3532 | Ring size 'US 7' has a space — expected 'US7' |
| A1036 | G3533 | Ring size 'US 7' has a space — expected 'US7' |
| A1037 | G3534 | Ring size 'US 7' has a space — expected 'US7' |
| A1038 | G3535 | Ring size 'US 7' has a space — expected 'US7' |
| A1039 | G3536 | Ring size 'US 7' has a space — expected 'US7' |
| A1040 | G3537 | Ring size 'US 7' has a space — expected 'US7' |
| A1116 | F3613 | Gold Details blank |
| A1171 | G3668 | Ring size 'US 11' has a space — expected 'US11' |
| A1172 | G3669 | Ring size 'US 7' has a space — expected 'US7' |
| A1173 | G3670 | Ring size 'US 7' has a space — expected 'US7' |
| A1174 | G3671 | Ring size 'US 7' has a space — expected 'US7' |
| A1175 | G3672 | Ring size 'US 7' has a space — expected 'US7' |
| A1176 | G3673 | Ring size 'US 7' has a space — expected 'US7' |
| A1177H | G3674 | Ring size 'US 7' has a space — expected 'US7' |
| A1182 | E3679 | LOCATION blank |
| A1182 | F3679 | Gold Details blank |
| A1182 | G3679 | INCH SIZE blank (only earrings/studs may be blank or NA) |
| A1182 | H3679 | GROSS WEIGHT blank |
| A1182 | I3679 | NET WEIGHT blank |
| A1183 | R3680 | Product Code blank while TDW = 7.28 |
| A1198 | R3695 | Product Code blank while TDW = 9.01 |
| A1199 | R3696 | Product Code blank while TDW = 20.74 |
| A1200 | R3697 | Product Code blank while TDW = 2.95 |
| A1201 | R3698 | Product Code blank while TDW = 15.45 |
| A1202 | R3699 | Product Code blank while TDW = 15.11 |
| A1203 | R3700 | Product Code blank while TDW = 15.56 |
| A1204 | R3701 | Product Code blank while TDW = 15.56 |
| A1205 | K3702 | Single row: breakup 4.75 != TDW 4.745 |
| A1206 | R3703 | Product Code blank while TDW = 14.65 |
| A1207 | R3704 | Product Code blank while TDW = 23.44 |
| A1208 | R3705 | Product Code blank while TDW = 16.22 |
| A1209 | R3706 | Product Code blank while TDW = 9.16 |
| A1247 | G3744 | Ring size 'US 7' has a space — expected 'US7' |
| A1250 | G3747 | Ring size 'US 7' has a space — expected 'US7' |
| A1407C | G3904 | Ring size 'US 7' has a space — expected 'US7' |
| A1626 | G4123 | Ring size 'US 7' has a space — expected 'US7' |
| A1627 | G4124 | Ring size 'US 7' has a space — expected 'US7' |
| A1628 | G4125 | Ring size 'US 7' has a space — expected 'US7' |
| A1629 | G4126 | Ring size 'US 7' has a space — expected 'US7' |
| A1630 | G4127 | Ring size 'US 7' has a space — expected 'US7' |
| A1631 | G4128 | Ring size 'US 7' has a space — expected 'US7' |
| A1632 | G4129 | Ring size 'US 7' has a space — expected 'US7' |
| A1633 | G4130 | Ring size 'US 7' has a space — expected 'US7' |
| A1634 | G4131 | Ring size 'US 7' has a space — expected 'US7' |
| A1635 | G4132 | Ring size 'US 7' has a space — expected 'US7' |
| A1636 | G4133 | Ring size 'US 7' has a space — expected 'US7' |
| A1637 | G4134 | Ring size 'US 7' has a space — expected 'US7' |
| A1638 | G4135 | Ring size 'US 7' has a space — expected 'US7' |
| A1639 | G4136 | Ring size 'US 7' has a space — expected 'US7' |
| A1640 | G4137 | Ring size 'US 7' has a space — expected 'US7' |
| A1641 | G4138 | Ring size 'US 7' has a space — expected 'US7' |
| A1642 | G4139 | Ring size 'US 7' has a space — expected 'US7' |
| A1643 | G4140 | Ring size 'US 7' has a space — expected 'US7' |
| A1644 | G4141 | Ring size 'US 7' has a space — expected 'US7' |
| A1645 | G4142 | Ring size 'US 7' has a space — expected 'US7' |
| A1646 | G4143 | Ring size 'US 7' has a space — expected 'US7' |
| A1647 | G4144 | Ring size 'US 7' has a space — expected 'US7' |
| A1648 | G4145 | Ring size 'US 7' has a space — expected 'US7' |
| A1649 | G4146 | Ring size 'US 7' has a space — expected 'US7' |
| A1650 | G4147 | Ring size 'US 7' has a space — expected 'US7' |
| A1651 | G4148 | Ring size 'US 7' has a space — expected 'US7' |
| A1652 | G4149 | Ring size 'US 7' has a space — expected 'US7' |
| A1653 | G4150 | Ring size 'US 7' has a space — expected 'US7' |
| A1654 | G4151 | Ring size 'US 7' has a space — expected 'US7' |
| A1655 | G4152 | Ring size 'US 7' has a space — expected 'US7' |
| A1656 | G4153 | Ring size 'US 7' has a space — expected 'US7' |
| A1657 | G4154 | Ring size 'US 7' has a space — expected 'US7' |
| A1658 | G4155 | Ring size 'US 7' has a space — expected 'US7' |
| A1659 | G4156 | Ring size 'US 7' has a space — expected 'US7' |
| A1660 | G4157 | Ring size 'US 7' has a space — expected 'US7' |
| A1661 | G4158 | Ring size 'US 7' has a space — expected 'US7' |
| A1665 | G4162 | Ring size 'US 7' has a space — expected 'US7' |
| A1666 | G4163 | Ring size 'US 7' has a space — expected 'US7' |
| A1667 | G4164 | Ring size 'US 7' has a space — expected 'US7' |
| A1668 | G4165 | Ring size 'US 7' has a space — expected 'US7' |
| A1669 | G4166 | Ring size 'US 7' has a space — expected 'US7' |
| A1670 | G4167 | Ring size 'US 7' has a space — expected 'US7' |
| A1671 | G4168 | Ring size 'US 7' has a space — expected 'US7' |
| A1672 | G4169 | Ring size 'US 7' has a space — expected 'US7' |
| A1673 | G4170 | Ring size 'US 7' has a space — expected 'US7' |
| A1674 | G4171 | Ring size 'US 7' has a space — expected 'US7' |
| A1675 | G4172 | Ring size 'US 7' has a space — expected 'US7' |
| A1676 | G4173 | Ring size 'US 7' has a space — expected 'US7' |
| A1677 | G4174 | Ring size 'US 7' has a space — expected 'US7' |
| A1678 | G4175 | Ring size 'US 7' has a space — expected 'US7' |
| A1679 | G4176 | Ring size 'US 7' has a space — expected 'US7' |
| A1680 | G4177 | Ring size 'US 7' has a space — expected 'US7' |
| A1681 | G4178 | Ring size 'US 7' has a space — expected 'US7' |
| A1940 | G4437 | Ring size 'US 7' has a space — expected 'US7' |
| A2201 | F4698 | Gold Details '10KT WHITE' — no 14KT/18KT found |
| A2438C | R4935 | Product Code '10/2 : 01' is not on the Price List |
| A2439C | R4936 | Product Code '10/2 : 01' is not on the Price List |
| A2440C | R4937 | Product Code '10/2 : 01' is not on the Price List |
| A2441C | R4938 | Product Code '10/2 : 01' is not on the Price List |
| 1802 | R748 | Multi Product Code blank while a diamond price is present |
| 358 | M355 | STOCK total pcs 179 != sum of Multi pcs 173 |
| 386 | M383 | STOCK total pcs 39 != sum of Multi pcs 37 |
| 480 | M477 | STOCK total pcs 38 != sum of Multi pcs 41 |
| 486 | M483 | STOCK total pcs 175 != sum of Multi pcs 173 |
| 487 | M484 | STOCK total pcs 175 != sum of Multi pcs 173 |
| 488 | M485 | STOCK total pcs 175 != sum of Multi pcs 173 |
| 489 | M486 | STOCK total pcs 175 != sum of Multi pcs 173 |
| 511 | M508 | STOCK total pcs 175 != sum of Multi pcs 173 |
| 647 | M644 | STOCK total pcs 127 != sum of Multi pcs 115 |
| 683 | M680 | STOCK total pcs 141 != sum of Multi pcs 143 |
| 785 | B272 | Multi date 2025-12-09 != STOCK date 2025-09-13 |
| 822 | B276 | Multi date 2025-09-14 != STOCK date 2025-09-15 |
| 831 | B318 | Multi date 2025-09-15 != STOCK date 2025-09-16 |
| 833 | B322 | Multi date 2025-09-15 != STOCK date 2025-09-16 |
| 835 | B315 | Multi date 2025-09-15 != STOCK date 2025-09-16 |
| 836 | B326 | Multi date 2025-09-15 != STOCK date 2025-09-16 |
| 837 | B328 | Multi date 2025-09-15 != STOCK date 2025-09-16 |
| 857 | J854 | STOCK TDW 2.1 != sum of Multi breakup 2.850 (difference -0.750) |
| 857 | M854 | STOCK total pcs 21 != sum of Multi pcs 80 |
| 858 | M855 | STOCK total pcs 82 != sum of Multi pcs 80 |
| 864 | M861 | STOCK total pcs 135 != sum of Multi pcs 63 |
| 932 | B434 | Multi date 2025-08-25 != STOCK date 2025-09-10 |
| 994 | J991 | STOCK TDW 8.21 != sum of Multi breakup 32.810 (difference -24.600) |
| 994 | M991 | STOCK total pcs 122 != sum of Multi pcs 96 |
| 1035 | J1032 | STOCK TDW 15.87 != sum of Multi breakup 16.090 (difference -0.220) |
| 1039 | M1036 | STOCK total pcs 14 != sum of Multi pcs 18 |
| 1099 | J1096 | STOCK TDW 10.2 != sum of Multi breakup 10.020 (difference +0.180) |
| 1101 | B570 | Multi date 2025-12-10 != STOCK date 2025-10-30 |
| 1155 | P1152 | Marked MIX on STOCK but there is no Multi group for this Sr |
| 1435 | M1432 | STOCK total pcs 60 != sum of Multi pcs 61 |
| 2106 | B1009 | Multi date 2026-12-27 != STOCK date 2025-12-27 |
| 1691 | J2227 | STOCK TDW 2.84 != sum of Multi breakup 17.380 (difference -14.540) |
| 1691 | M2227 | STOCK total pcs 244 != sum of Multi pcs 245 |
| 1692 | J2228 | STOCK TDW 6.58 != sum of Multi breakup 11.340 (difference -4.760) |
| 1692 | M2228 | STOCK total pcs 235 != sum of Multi pcs 230 |
| 1693 | J2229 | STOCK TDW 10.1 != sum of Multi breakup 16.620 (difference -6.520) |
| 1693 | M2229 | STOCK total pcs 212 != sum of Multi pcs 225 |
| 1694 | J2230 | STOCK TDW 16.95 != sum of Multi breakup 35.380 (difference -18.430) |
| 1694 | M2230 | STOCK total pcs 246 != sum of Multi pcs 302 |
| 1695 | J2231 | STOCK TDW 11.13 != sum of Multi breakup 12.050 (difference -0.920) |
| 1695 | M2231 | STOCK total pcs 485 != sum of Multi pcs 258 |
| 1696 | J2232 | STOCK TDW 0.92 != sum of Multi breakup 3.680 (difference -2.760) |
| 1697 | J2233 | STOCK TDW 1.02 != sum of Multi breakup 3.810 (difference -2.790) |
| 1698 | J2234 | STOCK TDW 0.78 != sum of Multi breakup 3.080 (difference -2.300) |
| 1699 | J2235 | STOCK TDW 0.8 != sum of Multi breakup 3.600 (difference -2.800) |
| 1699 | M2235 | STOCK total pcs 54 != sum of Multi pcs 136 |
| 1700 | J2236 | STOCK TDW 0.39 != sum of Multi breakup 7.320 (difference -6.930) |
| 1700 | M2236 | STOCK total pcs 48 != sum of Multi pcs 54 |
| 1701 | J2237 | STOCK TDW 0.72 != sum of Multi breakup 1.650 (difference -0.930) |
| 1701 | M2237 | STOCK total pcs 46 != sum of Multi pcs 48 |
| 1702 | J2238 | STOCK TDW 2.91 != sum of Multi breakup 3.140 (difference -0.230) |
| 1702 | M2238 | STOCK total pcs 336 != sum of Multi pcs 338 |
| 1703 | J2239 | STOCK TDW 1.4 != sum of Multi breakup 3.880 (difference -2.480) |
| 1703 | M2239 | STOCK total pcs 139 != sum of Multi pcs 141 |
| 1704 | J2240 | STOCK TDW 4.93 != sum of Multi breakup 84.630 (difference -79.700) |
| 1704 | M2240 | STOCK total pcs 364 != sum of Multi pcs 434 |
| 1705 | J2241 | STOCK TDW 0.62 != sum of Multi breakup 76.350 (difference -75.730) |
| 1705 | M2241 | STOCK total pcs 88 != sum of Multi pcs 154 |
| 1706 | J2242 | STOCK TDW 2.5 != sum of Multi breakup 23.050 (difference -20.550) |
| 1706 | M2242 | STOCK total pcs 197 != sum of Multi pcs 215 |
| 1707 | J2243 | STOCK TDW 61.389 != sum of Multi breakup 120.239 (difference -58.850) |
| 1707 | M2243 | STOCK total pcs 47 != sum of Multi pcs 149 |
| 1708 | J2244 | STOCK TDW 1.31 != sum of Multi breakup 32.700 (difference -31.390) |
| 1708 | M2244 | STOCK total pcs 72 != sum of Multi pcs 134 |
| 1709 | J2245 | STOCK TDW 13.78 != sum of Multi breakup 196.090 (difference -182.310) |
| 1709 | M2245 | STOCK total pcs 554 != sum of Multi pcs 730 |
| 1710 | J2246 | STOCK TDW 9.1 != sum of Multi breakup 84.880 (difference -75.780) |
| 1710 | M2246 | STOCK total pcs 186 != sum of Multi pcs 258 |
| 1711 | J2247 | STOCK TDW 39.88 != sum of Multi breakup 364.730 (difference -324.850) |
| 1712 | J2248 | STOCK TDW 7.16 != sum of Multi breakup 87.710 (difference -80.550) |
| 2253 | J2250 | STOCK TDW 11.14 != sum of Multi breakup 51.700 (difference -40.560) |
| 2254 | J2251 | STOCK TDW 2.77 != sum of Multi breakup 9.480 (difference -6.710) |
| 2255 | J2252 | STOCK TDW 10.29 != sum of Multi breakup 23.220 (difference -12.930) |
| 2256 | J2253 | STOCK TDW 5.55 != sum of Multi breakup 13.690 (difference -8.140) |
| 2259 | J2256 | STOCK TDW 67.37 != sum of Multi breakup 143.920 (difference -76.550) |
| 2260 | J2257 | STOCK TDW 5.91 != sum of Multi breakup 8.220 (difference -2.310) |
| 2261 | J2258 | STOCK TDW 32.43 != sum of Multi breakup 51.380 (difference -18.950) |
| 2261 | M2258 | STOCK total pcs 549 != sum of Multi pcs 558 |
| 2262 | J2259 | STOCK TDW 11.43 != sum of Multi breakup 22.210 (difference -10.780) |
| 2262 | M2259 | STOCK total pcs 216 != sum of Multi pcs 222 |
| 2263 | J2260 | STOCK TDW 32.63 != sum of Multi breakup 71.440 (difference -38.810) |
| 2264 | J2261 | STOCK TDW 7.41 != sum of Multi breakup 26.880 (difference -19.470) |
| 2267 | J2264 | STOCK TDW 31.02 != sum of Multi breakup 41.680 (difference -10.660) |
| 2267 | M2264 | STOCK total pcs 346 != sum of Multi pcs 353 |
| 2268 | J2265 | STOCK TDW 7.83 != sum of Multi breakup 14.095 (difference -6.265) |
| 2269 | J2266 | STOCK TDW 23.59 != sum of Multi breakup 52.990 (difference -29.400) |
| 2270 | J2267 | STOCK TDW 8.25 != sum of Multi breakup 17.000 (difference -8.750) |
| 2270 | B1200 | Multi date 2025-06-01 != STOCK date 2026-06-01 |
| 2271 | J2268 | STOCK TDW 24.83 != sum of Multi breakup 47.980 (difference -23.150) |
| 2271 | M2268 | STOCK total pcs 369 != sum of Multi pcs 378 |
| 2272 | J2269 | STOCK TDW 7.21 != sum of Multi breakup 15.660 (difference -8.450) |
| 2272 | M2269 | STOCK total pcs 108 != sum of Multi pcs 110 |
| 2275 | J2272 | STOCK TDW 30.28 != sum of Multi breakup 89.970 (difference -59.690) |
| 2276 | J2273 | STOCK TDW 10.03 != sum of Multi breakup 27.340 (difference -17.310) |
| 2277 | M2274 | STOCK total pcs 236 != sum of Multi pcs 238 |
| 2279 | J2276 | STOCK TDW 133.84 != sum of Multi breakup 409.470 (difference -275.630) |
| 2279 | M2276 | STOCK total pcs 1723 != sum of Multi pcs 2010 |
| 2280 | J2277 | STOCK TDW 7.65 != sum of Multi breakup 121.930 (difference -114.280) |
| 2280 | M2277 | STOCK total pcs 652 != sum of Multi pcs 732 |
| 2281 | J2278 | STOCK TDW 35.55 != sum of Multi breakup 121.940 (difference -86.390) |
| 2282 | J2279 | STOCK TDW 12.4 != sum of Multi breakup 38.780 (difference -26.380) |
| 2283 | J2280 | STOCK TDW 81.53 != sum of Multi breakup 158.040 (difference -76.510) |
| 2283 | M2280 | STOCK total pcs 1014 != sum of Multi pcs 1092 |
| 2283 | B1319 | Multi date 0206-01-07 != STOCK date 2026-07-01 |
| 2284 | J2281 | STOCK TDW 20.85 != sum of Multi breakup 46.630 (difference -25.780) |
| 2284 | M2281 | STOCK total pcs 434 != sum of Multi pcs 460 |
| 2285 | J2282 | STOCK TDW 11.21 != sum of Multi breakup 124.880 (difference -113.670) |
| 2286 | J2283 | STOCK TDW 14.29 != sum of Multi breakup 40.010 (difference -25.720) |
| 2287 | J2284 | STOCK TDW 36.14 != sum of Multi breakup 115.400 (difference -79.260) |
| 2288 | J2285 | STOCK TDW 13.15 != sum of Multi breakup 45.620 (difference -32.470) |
| 2290 | J2287 | STOCK TDW 9.02 != sum of Multi breakup 10.620 (difference -1.600) |
| 2291 | J2288 | STOCK TDW 107.1 != sum of Multi breakup 147.680 (difference -40.580) |
| 2291 | M2288 | STOCK total pcs 1014 != sum of Multi pcs 923 |
| 2292 | J2289 | STOCK TDW 41.79 != sum of Multi breakup 53.640 (difference -11.850) |
| 2306 | M2303 | STOCK total pcs 36 != sum of Multi pcs 37 |
| 2309 | M2306 | STOCK total pcs 36 != sum of Multi pcs 37 |
| A0034 | B1596 | Multi date 2026-01-16 != STOCK date 2026-01-15 |
| A0310 | J2807 | STOCK TDW 18.77 != sum of Multi breakup 75.240 (difference -56.470) |
| A0311 | J2808 | STOCK TDW 9.5 != sum of Multi breakup 40.170 (difference -30.670) |
| A0312 | J2809 | STOCK TDW 210.73 != sum of Multi breakup 381.630 (difference -170.900) |
| A0313 | J2810 | STOCK TDW 9.27 != sum of Multi breakup 80.440 (difference -71.170) |
| A0314 | J2811 | STOCK TDW 19.18 != sum of Multi breakup 219.720 (difference -200.540) |
| A0315 | J2812 | STOCK TDW 37.02 != sum of Multi breakup 36.550 (difference +0.470) |
| A0316 | J2813 | STOCK TDW 95.34 != sum of Multi breakup 142.860 (difference -47.520) |
| A0316 | M2813 | STOCK total pcs 16.9 != sum of Multi pcs 2010 |
| A0400 | J2897 | STOCK TDW 7.72 != sum of Multi breakup 45.860 (difference -38.140) |
| A0400 | M2897 | STOCK total pcs 612 != sum of Multi pcs 614 |
| A0410 | J2907 | STOCK TDW 26.78 != sum of Multi breakup 33.260 (difference -6.480) |
| A0411 | J2908 | STOCK TDW 11.13 != sum of Multi breakup 17.030 (difference -5.900) |
| A0468 | M2965 | STOCK total pcs 36 != sum of Multi pcs 37 |
| A0493 | J2990 | STOCK TDW 34.03 != sum of Multi breakup 77.770 (difference -43.740) |
| A0494 | J2991 | STOCK TDW 8.52 != sum of Multi breakup 14.370 (difference -5.850) |
| A0580 | J3077 | STOCK TDW 5.43 != sum of Multi breakup 5.350 (difference +0.080) |
| A0631 | J3128 | STOCK TDW 31.66 != sum of Multi breakup 36.500 (difference -4.840) |
| A0632 | J3129 | STOCK TDW 10.84 != sum of Multi breakup 15.160 (difference -4.320) |
| A0657 | J3154 | STOCK TDW 11.31 != sum of Multi breakup 204.670 (difference -193.360) |
| A0657 | M3154 | STOCK total pcs 1125 != sum of Multi pcs 991 |
| A0658 | J3155 | STOCK TDW 2.91 != sum of Multi breakup 49.660 (difference -46.750) |
| A0658 | M3155 | STOCK total pcs 280 != sum of Multi pcs 262 |
| A0659 | J3156 | STOCK TDW 3.67 != sum of Multi breakup 7.670 (difference -4.000) |
| A0660 | J3157 | STOCK TDW 6.01 != sum of Multi breakup 151.170 (difference -145.160) |
| A0660 | M3157 | STOCK total pcs 518 != sum of Multi pcs 438 |
| A0661 | J3158 | STOCK TDW 2.38 != sum of Multi breakup 68.620 (difference -66.240) |
| A0661 | M3158 | STOCK total pcs 260 != sum of Multi pcs 220 |
| A0704 | J3201 | STOCK TDW 22.69 != sum of Multi breakup 125.520 (difference -102.830) |
| A0704 | M3201 | STOCK total pcs 790 != sum of Multi pcs 729 |
| A0705 | J3202 | STOCK TDW 6.05 != sum of Multi breakup 47.190 (difference -41.140) |
| A0705 | M3202 | STOCK total pcs 354 != sum of Multi pcs 334 |
| A0706 | J3203 | STOCK TDW 8.39 != sum of Multi breakup 131.870 (difference -123.480) |
| A0706 | M3203 | STOCK total pcs 768 != sum of Multi pcs 712 |
| A0707 | J3204 | STOCK TDW 8.68 != sum of Multi breakup 110.030 (difference -101.350) |
| A0707 | M3204 | STOCK total pcs 982 != sum of Multi pcs 912 |
| A0708 | J3205 | STOCK TDW 7.3 != sum of Multi breakup 102.650 (difference -95.350) |
| A0708 | M3205 | STOCK total pcs 731 != sum of Multi pcs 694 |
| A0709 | J3206 | STOCK TDW 2.55 != sum of Multi breakup 43.010 (difference -40.460) |
| A0709 | M3206 | STOCK total pcs 236 != sum of Multi pcs 214 |
| A0758 | J3255 | STOCK TDW 1.2 != sum of Multi breakup 1.130 (difference +0.070) |
| A0765 | J3262 | STOCK TDW 6.78 != sum of Multi breakup 25.160 (difference -18.380) |
| A0765 | M3262 | STOCK total pcs 508 != sum of Multi pcs 618 |
| A0782 | J3279 | STOCK TDW 1.66 != sum of Multi breakup 8.920 (difference -7.260) |
| A0782 | M3279 | STOCK total pcs 89 != sum of Multi pcs 97 |
| A0838CH | M3335 | STOCK total pcs 218 != sum of Multi pcs 219 |
| A0893 | J3390 | STOCK TDW 2.92 != sum of Multi breakup 2.910 (difference +0.010) |
| A0894 | J3391 | STOCK TDW 2.89 != sum of Multi breakup 2.880 (difference +0.010) |
| A0895 | J3392 | STOCK TDW 2.88 != sum of Multi breakup 2.870 (difference +0.010) |
| A0946 | B2533 | Multi date 2026-10-03 != STOCK date 2026-09-03 |
| A0947 | B2541 | Multi date 2026-10-03 != STOCK date 2026-09-03 |
| A0948 | B2549 | Multi date 2026-10-03 != STOCK date 2026-09-03 |
| A0949 | B2557 | Multi date 2026-10-03 != STOCK date 2026-09-03 |
| A0986 | B2608 | Multi date 2026-11-03 != STOCK date 2025-11-03 |
| A1024 | J3521 | STOCK TDW 11.76 != sum of Multi breakup 41.760 (difference -30.000) |
| A1024 | M3521 | STOCK total pcs 347 != sum of Multi pcs 317 |
| A1153 | J3650 | STOCK TDW 8.42 != sum of Multi breakup 8.425 (difference -0.005) |
| A1199 | M3696 | STOCK total pcs 459 != sum of Multi pcs 294 |
| A1200 | J3697 | STOCK TDW 2.95 != sum of Multi breakup 31.650 (difference -28.700) |
| A1200 | M3697 | STOCK total pcs 60 != sum of Multi pcs 30 |
| A1203 | J3700 | STOCK TDW 15.56 != sum of Multi breakup 15.552 (difference +0.008) |
| A1381 | M3878 | STOCK total pcs 214 != sum of Multi pcs 194 |
| A1383 | J3880 | STOCK TDW 10.31 != sum of Multi breakup 10.480 (difference -0.170) |
| A1402CZ | J3899 | STOCK TDW 113.75 != sum of Multi breakup 136.200 (difference -22.450) |
| A1402CZ | M3899 | STOCK total pcs 1055 != sum of Multi pcs 1059 |
| A1403 | J3900 | STOCK TDW 64.2 != sum of Multi breakup 86.650 (difference -22.450) |
| A1403 | M3900 | STOCK total pcs 1055 != sum of Multi pcs 1059 |
| A1404 | J3901 | STOCK TDW 65.65 != sum of Multi breakup 88.100 (difference -22.450) |
| A1404 | M3901 | STOCK total pcs 1055 != sum of Multi pcs 1059 |
| A1405CZ | J3902 | STOCK TDW 114.1 != sum of Multi breakup 136.550 (difference -22.450) |
| A1405CZ | M3902 | STOCK total pcs 1055 != sum of Multi pcs 1059 |
| A1406CZ | J3903 | STOCK TDW 112.6 != sum of Multi breakup 135.050 (difference -22.450) |
| A1406CZ | M3903 | STOCK total pcs 1055 != sum of Multi pcs 1059 |
| A1624 | J4121 | STOCK TDW 15.28 != sum of Multi breakup 158.820 (difference -143.540) |
| A1624 | M4121 | STOCK total pcs 1197 != sum of Multi pcs 1530 |
| A1625 | J4122 | STOCK TDW 2.24 != sum of Multi breakup 19.990 (difference -17.750) |
| A1625 | M4122 | STOCK total pcs 392 != sum of Multi pcs 454 |
| A1929 | J4426 | STOCK TDW 6.02 != sum of Multi breakup 54.840 (difference -48.820) |
| A1929 | M4426 | STOCK total pcs 649 != sum of Multi pcs 893 |
| A1930 | J4427 | STOCK TDW 1.26 != sum of Multi breakup 38.360 (difference -37.100) |
| A1930 | M4427 | STOCK total pcs 172 != sum of Multi pcs 272 |
| A2201 | J4698 | STOCK TDW 3.553 != sum of Multi breakup 3.574 (difference -0.021) |

## Summary by rule

| Count | Rule |
|---|---|
| 559 | Design Number blank while TDW = 3 |
| 429 | Design Number blank while TDW = 5 |
| 368 | Design Number blank while TDW = 7 |
| 331 | Design Number blank while TDW = 10 |
| 312 | Ring size 'US 7' has a space — expected 'US7' |
| 229 | Design Number blank while TDW = 4 |
| 201 | Design Number blank while TDW = 2 |
| 136 | Design Number blank while TDW = 1 |
| 82 | Design Number blank while TDW = 9 |
| 39 | Design Number blank while TDW = 6 |
| 23 | Design Number blank while TDW = 15 |
| 22 | Design Number blank while TDW = 0 |
| 16 | Design Number blank while TDW = 11 |
| 15 | Design Number blank while TDW = 12 |
| 13 | STOCK TDW 2 |
| 12 | Design Number blank while TDW = 14 |
| 10 | Design Number blank while TDW = 13 |
| 9 | Design Number blank while TDW = 23 |
| 8 | GROSS WEIGHT is zero |
| 8 | Design Number blank while TDW = 8 |
| 8 | Design Number blank while TDW = 16 |
| 7 | STOCK TDW 11 |
| 7 | STOCK TDW 7 |
| 6 | STOCK TDW 8 |
| 6 | STOCK TDW 10 |
| 6 | STOCK TDW 0 |
| 6 | STOCK TDW 1 |
| 5 | Design Number blank while TDW = 37 |
| 5 | Design Number blank while TDW = 32 |
| 5 | STOCK total pcs 175 != sum of Multi pcs 173 |
| 5 | Multi date 2025-09-15 != STOCK date 2025-09-16 |
| 5 | STOCK TDW 6 |
| 5 | STOCK total pcs 1055 != sum of Multi pcs 1059 |
| 4 | Design Number blank while TDW = 38 |
| 4 | Design Number blank while TDW = 30 |
| 4 | Design Number blank while TDW = 29 |
| 4 | Design Number blank while TDW = 36 |
| 4 | Design Number blank while TDW = 26 |
| 4 | Design Number blank while TDW = 31 |
| 4 | Product Code blank while TDW = 15 |
| 4 | Product Code '10/2 : 01' is not on the Price List |
| 4 | STOCK TDW 9 |
| 4 | Multi date 2026-10-03 != STOCK date 2026-09-03 |
| 3 | Design Number blank while TDW = 21 |
| 3 | Design Number blank while TDW = 27 |
| 3 | Design Number blank while TDW = 22 |
| 3 | Design Number blank while TDW = 20 |
| 3 | Design Number blank while TDW = 65 |
| 3 | Design Number blank while TDW = 35 |
| 3 | Design Number blank while TDW = 19 |
| 3 | STOCK TDW 15 |
| 3 | STOCK TDW 5 |
| 3 | STOCK total pcs 36 != sum of Multi pcs 37 |
| 2 | Product Code '0 |
| 2 | Design Number blank while TDW = 25 |
| 2 | Design Number blank while TDW = 24 |
| 2 | Design Number blank while TDW = 39 |
| 2 | Design Number blank while TDW = 34 |
| 2 | GROSS WEIGHT blank |
| 2 | NET WEIGHT blank |
| 2 | Design Number blank while TDW = 17 |
| 2 | Design Number blank while TDW = 33 |
| 2 | Gold Details blank |
| 2 | Product Code blank while TDW = 9 |
| 2 | STOCK TDW 13 |
| 2 | STOCK TDW 32 |
| 2 | STOCK TDW 31 |
| 2 | STOCK TDW 3 |
| 1 | TDW = 0 but net 11 |
| 1 | Single row: breakup 80 |
| 1 | Design Number blank while TDW = 80 |
| 1 | Ring size 'US  7' has a space — expected 'US7' |
| 1 | Design Number blank while TDW = 75 |
| 1 | Design Number blank while TDW = 110 |
| 1 | Design Number blank while TDW = 105 |
| 1 | Gold Details '14 WHITE' — no 14KT/18KT found |
| 1 | Design Number blank while TDW = 44 |
| 1 | Net 12 |
| 1 | Gold Details 'SILVER' — no 14KT/18KT found |
| 1 | Ring size 'US 14' has a space — expected 'US14' |
| 1 | Net 5 |
| 1 | Design Number blank while TDW = 61 |
| 1 | Row has a Sr number but is otherwise empty |
| 1 | Design Number blank while TDW = 67 |
| 1 | Design Number blank while TDW = 43 |
| 1 | Design Number blank while TDW = 133 |
| 1 | Design Number blank while TDW = 81 |
| 1 | Net 59 |
| 1 | Design Number blank while TDW = 107 |
| 1 | Design Number blank while TDW = 41 |
| 1 | Design Number blank while TDW = 28 |
| 1 | Design Number blank while TDW = 45 |
| 1 | Design Number blank while TDW = 18 |
| 1 | Design Number blank while TDW = 210 |
| 1 | Design Number blank while TDW = 95 |
| 1 | Ring size 'US 4' has a space — expected 'US4' |
| 1 | Product Code blank while TDW = 5 |
| 1 | Product Code blank while TDW = 3 |
| 1 | Ring size 'US 11' has a space — expected 'US11' |
| 1 | LOCATION blank |
| 1 | INCH SIZE blank |
| 1 | Product Code blank while TDW = 7 |
| 1 | Product Code blank while TDW = 20 |
| 1 | Product Code blank while TDW = 2 |
| 1 | Single row: breakup 4 |
| 1 | Product Code blank while TDW = 14 |
| 1 | Product Code blank while TDW = 23 |
| 1 | Product Code blank while TDW = 16 |
| 1 | Gold Details '10KT WHITE' — no 14KT/18KT found |
| 1 | Multi Product Code blank while a diamond price is present |
| 1 | STOCK total pcs 179 != sum of Multi pcs 173 |
| 1 | STOCK total pcs 39 != sum of Multi pcs 37 |
| 1 | STOCK total pcs 38 != sum of Multi pcs 41 |
| 1 | STOCK total pcs 127 != sum of Multi pcs 115 |
| 1 | STOCK total pcs 141 != sum of Multi pcs 143 |
| 1 | Multi date 2025-12-09 != STOCK date 2025-09-13 |
| 1 | Multi date 2025-09-14 != STOCK date 2025-09-15 |
| 1 | STOCK total pcs 21 != sum of Multi pcs 80 |
| 1 | STOCK total pcs 82 != sum of Multi pcs 80 |
| 1 | STOCK total pcs 135 != sum of Multi pcs 63 |
| 1 | Multi date 2025-08-25 != STOCK date 2025-09-10 |
| 1 | STOCK total pcs 122 != sum of Multi pcs 96 |
| 1 | STOCK total pcs 14 != sum of Multi pcs 18 |
| 1 | Multi date 2025-12-10 != STOCK date 2025-10-30 |
| 1 | Marked MIX on STOCK but there is no Multi group for this Sr |
| 1 | STOCK total pcs 60 != sum of Multi pcs 61 |
| 1 | Multi date 2026-12-27 != STOCK date 2025-12-27 |
| 1 | STOCK total pcs 244 != sum of Multi pcs 245 |
| 1 | STOCK total pcs 235 != sum of Multi pcs 230 |
| 1 | STOCK total pcs 212 != sum of Multi pcs 225 |
| 1 | STOCK TDW 16 |
| 1 | STOCK total pcs 246 != sum of Multi pcs 302 |
| 1 | STOCK total pcs 485 != sum of Multi pcs 258 |
| 1 | STOCK total pcs 54 != sum of Multi pcs 136 |
| 1 | STOCK total pcs 48 != sum of Multi pcs 54 |
| 1 | STOCK total pcs 46 != sum of Multi pcs 48 |
| 1 | STOCK total pcs 336 != sum of Multi pcs 338 |
| 1 | STOCK total pcs 139 != sum of Multi pcs 141 |
| 1 | STOCK TDW 4 |
| 1 | STOCK total pcs 364 != sum of Multi pcs 434 |
| 1 | STOCK total pcs 88 != sum of Multi pcs 154 |
| 1 | STOCK total pcs 197 != sum of Multi pcs 215 |
| 1 | STOCK TDW 61 |
| 1 | STOCK total pcs 47 != sum of Multi pcs 149 |
| 1 | STOCK total pcs 72 != sum of Multi pcs 134 |
| 1 | STOCK total pcs 554 != sum of Multi pcs 730 |
| 1 | STOCK total pcs 186 != sum of Multi pcs 258 |
| 1 | STOCK TDW 39 |
| 1 | STOCK TDW 67 |
| 1 | STOCK total pcs 549 != sum of Multi pcs 558 |
| 1 | STOCK total pcs 216 != sum of Multi pcs 222 |
| 1 | STOCK total pcs 346 != sum of Multi pcs 353 |
| 1 | STOCK TDW 23 |
| 1 | Multi date 2025-06-01 != STOCK date 2026-06-01 |
| 1 | STOCK TDW 24 |
| 1 | STOCK total pcs 369 != sum of Multi pcs 378 |
| 1 | STOCK total pcs 108 != sum of Multi pcs 110 |
| 1 | STOCK TDW 30 |
| 1 | STOCK total pcs 236 != sum of Multi pcs 238 |
| 1 | STOCK TDW 133 |
| 1 | STOCK total pcs 1723 != sum of Multi pcs 2010 |
| 1 | STOCK total pcs 652 != sum of Multi pcs 732 |
| 1 | STOCK TDW 35 |
| 1 | STOCK TDW 12 |
| 1 | STOCK TDW 81 |
| 1 | STOCK total pcs 1014 != sum of Multi pcs 1092 |
| 1 | Multi date 0206-01-07 != STOCK date 2026-07-01 |
| 1 | STOCK TDW 20 |
| 1 | STOCK total pcs 434 != sum of Multi pcs 460 |
| 1 | STOCK TDW 14 |
| 1 | STOCK TDW 36 |
| 1 | STOCK TDW 107 |
| 1 | STOCK total pcs 1014 != sum of Multi pcs 923 |
| 1 | STOCK TDW 41 |
| 1 | Multi date 2026-01-16 != STOCK date 2026-01-15 |
| 1 | STOCK TDW 18 |
| 1 | STOCK TDW 210 |
| 1 | STOCK TDW 19 |
| 1 | STOCK TDW 37 |
| 1 | STOCK TDW 95 |
| 1 | STOCK total pcs 16 |
| 1 | STOCK total pcs 612 != sum of Multi pcs 614 |
| 1 | STOCK TDW 26 |
| 1 | STOCK TDW 34 |
| 1 | STOCK total pcs 1125 != sum of Multi pcs 991 |
| 1 | STOCK total pcs 280 != sum of Multi pcs 262 |
| 1 | STOCK total pcs 518 != sum of Multi pcs 438 |
| 1 | STOCK total pcs 260 != sum of Multi pcs 220 |
| 1 | STOCK TDW 22 |
| 1 | STOCK total pcs 790 != sum of Multi pcs 729 |
| 1 | STOCK total pcs 354 != sum of Multi pcs 334 |
| 1 | STOCK total pcs 768 != sum of Multi pcs 712 |
| 1 | STOCK total pcs 982 != sum of Multi pcs 912 |
| 1 | STOCK total pcs 731 != sum of Multi pcs 694 |
| 1 | STOCK total pcs 236 != sum of Multi pcs 214 |
| 1 | STOCK total pcs 508 != sum of Multi pcs 618 |
| 1 | STOCK total pcs 89 != sum of Multi pcs 97 |
| 1 | STOCK total pcs 218 != sum of Multi pcs 219 |
| 1 | Multi date 2026-11-03 != STOCK date 2025-11-03 |
| 1 | STOCK total pcs 347 != sum of Multi pcs 317 |
| 1 | STOCK total pcs 459 != sum of Multi pcs 294 |
| 1 | STOCK total pcs 60 != sum of Multi pcs 30 |
| 1 | STOCK total pcs 214 != sum of Multi pcs 194 |
| 1 | STOCK TDW 113 |
| 1 | STOCK TDW 64 |
| 1 | STOCK TDW 65 |
| 1 | STOCK TDW 114 |
| 1 | STOCK TDW 112 |
| 1 | STOCK total pcs 1197 != sum of Multi pcs 1530 |
| 1 | STOCK total pcs 392 != sum of Multi pcs 454 |
| 1 | STOCK total pcs 649 != sum of Multi pcs 893 |
| 1 | STOCK total pcs 172 != sum of Multi pcs 272 |

## Questions for Deval (7)

| Stock # | Cell | Question |
|---|---|---|
| ALL | Price List B68 | The B-column price list is exactly full to row 68, the same row every VLOOKUP caps at. The next code added lands outside the range. Extend the ranges before adding one? |
| ALL | Price List J68 | The J-column price list is exactly full to row 68, the same row every VLOOKUP caps at. The next code added lands outside the range. Extend the ranges before adding one? |
| 527 | E524 | Location '0.0' is not in the allowed list. New location, or a typo? |
| 849 | E846 | Location '0.0' is not in the allowed list. New location, or a typo? |
| 1034 | E1031 | Location '0.0' is not in the allowed list. New location, or a typo? |
| 1139 | E1136 | Location '0.0' is not in the allowed list. New location, or a typo? |
| 1648 | E1645 | Location '0.0' is not in the allowed list. New location, or a typo? |
