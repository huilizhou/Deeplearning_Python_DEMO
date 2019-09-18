fi = open("侠客行-网络版.txt", "r", encoding='utf-8')
fo = open("侠客行-字符统计.txt", "w", encoding='utf-8')
txt = fi.read()
d = {}
for c in txt:
    if 0x4e00 <= ord(c) <= 0x9fa5:
        d[c] = d.get(c, 0) + 1
ls = []
for key in d:
    ls.append("{}(0x{:x}):{}".format(key, ord(key), d[key]))
fo.write(",".join(ls))
fi.close()
fo.close()
