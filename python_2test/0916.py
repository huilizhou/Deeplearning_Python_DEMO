ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合",
      "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合", "理工",
      "理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工",
      "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]

d = {}
for i in ls:
    d[i] = d.get(i, 0) + 1
for k in d:
    print('{}:{}'.format(k, d[k]))
    # print(k + ':' + d[k])
