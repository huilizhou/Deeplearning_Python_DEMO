# N = input()
# sum = 0
# for i in range(1, eval(N)):
#     if i % 2 == 1:
#         sum += i**2
# print(sum)


# N = input()

# for i in range(2, eval(N)):
#     if eval(N) % i == 0:
#         print(False)
# print(True)


# N = eval(input())
# if N == 1:
#     flag = False
#     print(flag)
# else:
#     flag = True
#     for i in range(2, N):
#         if N % i == 0:
#             flag = False
#             break
#     print(flag)


# print(','.join(['1', '2', '3']))


# import random as r
# r.seed(17)
# s = ""
# for i in range(20):
#     s += str(r.randint(0, 999))
# print(s)

# import turtle
# for i in range(4):
#     turtle.right(90)
#     turtle.circle(50, 180)


# import turtle
# for i in range(4):
#     turtle.circle(-90, 90)
#     turtle.right(180)


# import turtle
# edge = 5
# d = 0
# k = 1
# for j in range(10):
#     for i in range(edge):
#         turtle.fd(k)
#         d += 360 / edge
#         turtle.seth(d)
#         k += 3
# turtle.done()


# 可参照编程模板，完善代码实现图形绘制，亦可以自行设计编码实现。
import turtle
# 定义绘制菱形函数


def Draw():
    # 开始填充颜色
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.end_fill()


for i in range(3):
    turtle.fillcolor("green")
    Draw()
turtle.left(60)
