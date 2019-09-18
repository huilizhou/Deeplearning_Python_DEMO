fi = open('孙子兵法-网络版.txt', 'r')
fo = open('孙子兵法-清洗版.txt', 'w')
for line in fi:
    if '作者' in line:
        continue
    if '【' in line:
        continue
    for c in '@!#':
        line = line.replace(c, '')
    fo.write(line)

fi.close()
fo.close()
