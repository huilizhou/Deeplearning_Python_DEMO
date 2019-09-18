# 四个等边三角形

# import turtle
# turtle.pensize(2)  # 设置画笔宽度为2像素
# turtle.color('red')
# turtle.fd(160)  # 向小海龟当前行进方向前进160像素
# turtle.seth(120)
# turtle.fd(160)
# turtle.seth(-120)
# turtle.fd(160)
# turtle.penup()
# turtle.seth(0)
# turtle.fd(80)
# turtle.pendown()
# turtle.seth(60)
# turtle.fd(80)
# turtle.seth(180)
# turtle.fd(80)
# turtle.seth(-60)
# turtle.fd(80)
# turtle.hideturtle()
# turtle.done()


# import turtle as t
# t.colormode(255)
# t.color(255, 215, 0)  # 设置颜色取值为金色（255,215,0）
# t.begin_fill()
# for x in range(8):  # 绘制8条线
#     t.forward(200)
#     t.left(225)
# t.end_fill()
# t.hideturtle()
# t.done()

# 画多边形
# from turtle import *
# for i in range(5):
#     penup()  # 画笔抬起
#     goto(-200 + 100 * i, -50)
#     pendown()
#     circle(40, steps=3 + i)  # 画某个形状
# done()


import turtle as t


def tree(length, level):  # 树的层次
    if level <= 0:
        return
    t.forward(length)  # 前进方向画 length距离

    t.left(45)
    tree(0.6 * length, level - 1)
    t.right(90)
    tree(0.6 * length, level - 1)
    t.left(45)
    t.backward(length)
    return


t.pensize(3)
t.color('green')
t.left(90)
tree(100, 6)
