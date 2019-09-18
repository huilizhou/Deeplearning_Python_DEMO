fi = open("笑傲江湖-网络版.txt", "r", encoding='utf-8')
txt = fi.read()
cnt = 0
flag = False
for c in txt:
    if c == "“":
        flag = True
    if c == "”":
        flag = False
    if flag:
        cnt += 1
print("占总字符比例：{:.0%}。".format(cnt / len(txt)))
fi.close()
