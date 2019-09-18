import jieba
fi = open("神雕侠侣-网络版.txt", "r", encoding='utf-8')
fo = open("神雕侠侣-人名亲和度.txt", "w", encoding='utf-8')
names = ["杨过", "小龙女", "李莫愁", "裘千尺", "郭靖", "黄蓉"]
d = {}
for item1 in names:
    for item2 in names:
        if item1 != item2:
            d[item1 + "-" + item2] = 0
txt = fi.read()
ls = jieba.lcut(txt)

for i in range(len(ls) - 100):
    if ls[i] in names:
        for j in range(1, 101):
            if ls[i + j] != ls[i] and (ls[i + j] in names):
                d[ls[i] + '-' + ls[i + j]] += 1
                break
ols = []
for key in d:
    ols.append("{}:{}".format(key, d[key]))
fo.write(",".join(ols))
# fo.write(",\n".join(ols))
fi.close()
fo.close()
