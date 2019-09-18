ls = []
for i in range(1, 11):
    fo = open(str(i) + ".csv", "r", encoding="utf-8")
    for line in fo:
        line = line.replace("\n", "")
        ls.append(line.split(",")[0])
    fo.close()
counts = {}
for name in ls:
    counts[name] = counts.get(name, 0) + 1
items = list(counts.items())
print("全勤同学有：", end="")
for i in range(1, 75, 1):
    word, count = items[i]
    if count == 10:
        print(word, end=",")
