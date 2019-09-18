# import turtle


# turtle.pensize(3)
# turtle.circle(20)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)


# x = 2
# y = 3
# print(x)

# s = '等级'

# print("{:*<25}".format(s))


# s = 'an apple a day'


# def split(s):
#     return s.split('a')


# print(s.split())
# print(split(s))


# def func():
#     print('Hello')


# print(type(func), type(func()))


# def func(ls=[]):
#     ls.append(1)
#     return ls


# a = func()
# b = func()
# print(a, b)

# d = {'1': 1, '2': 2, '3': 3, '4': 4}
# d2 = d
# d['2'] = 5
# print(d)
# print(d2)


# L = [1, 2, 3, 4]
# print(L.pop())

# import turtle

# turtle.circle(180)

# import jieba

# print(jieba.lcut('全国计算机等级考试'))

import turtle

turtle.pensize(4)
turtle.pencolor('yellow')
turtle.fillcolor('red')
turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
