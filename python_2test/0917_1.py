# # s=input()
# s = '1,2,3,4'
# m = max(s.split(','))
# print(m)

# data = input()
# a = data.split(",")
# b = []
# for i in a:
#     b.append(int(i))
# print(max(b))

# print('True')


# print(pow(2, 10, 100))


# 画爱心
# from turtle import *
# color('red', 'pink')
# begin_fill()
# left(135)
# fd(100)
# right(180)
# circle(50, -180)
# left(90)
# circle(50, -180)
# right(180)
# fd(100)
# end_fill()
# hideturtle()
# done()


# 五角星
# from turtle import *
# setup(400, 400)
# penup()
# goto(-100, 50)
# pendown()
# color("red")
# begin_fill()
# for i in range(5):
#     forward(200)
#     right(144)
# end_fill()
# hideturtle()
# done()

# 画同心圆
# import turtle as t
# def DrwaCctCircle(n):
#     t.penup()
#     t.goto(0, -n)
#     t.pendown()
#     t.circle(n)


# for i in range(20, 100, 20):
#     DrwaCctCircle(i)
# t.hideturtle()
# t.done()


import turtle as t
t.setup(500, 300)
t.penup()
t.goto(-180, -50)  # 将画笔移动到绝对位置(-180,-50)处
t.pendown()  # 画笔落下


def Drawrect():
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.penup()
    t.left(90)
    t.fd(42)
    t.pendown()


for i in range(7):
    Drawrect()
t.penup()
t.goto(-150, 0)
t.pendown


def DrawRectBlack():
    t.color('black')
    t.begin_fill()
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(40)
    t.pendown()


DrawRectBlack()
DrawRectBlack()
t.penup()
t.fd(48)
t.pendown()
DrawRectBlack()
DrawRectBlack()
DrawRectBlack()
t.hideturtle()
t.done()
