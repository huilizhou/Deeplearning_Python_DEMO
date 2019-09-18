import jieba
import random

s = "今天北京有个好天气，大家一起去爬山。"
k = s.find('，')
s1 = jieba.lcut(s[0:k])
s2 = jieba.lcut(s[k + 1:-1])
random.seed(8)
lines = []
while True:
    line = ""
    random.shuffle(s1)
    random.shuffle(s2)
    for item in s1:
        line += item
    line += '，'
    for item in s2:
        line += item
    line += '。'
    if line in lines:
        continue
    else:
        lines.append(line)
    if len(lines) == 10:
        break

fo = open('句子组合.txt', 'w')
fo.write('\n'.join(lines))
fo.close()
