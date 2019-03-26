# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])

# p = Point(1, 2)
# print(p.x, p.y)


# def sum_2_num(num1, num2):
#     result = num1 + num2

#     return result


# print(sum_2_num(2, 3))


# def print_line(char, times):
#     print(char * times)


# def print_lines(char, times, i):
#     row = 0
#     while row <= i:
#         print_line(char, times)
#         row += 1


# print_lines("^", 30)

# card_list = [
#     {'name': 'zhangsan',
#      'phone': 10089},
#     {'name': 'lisi',
#      'phone': 10087}
# ]

# for card_info in card_list:
#     print(card_info)

# poem = ["\t\n咏鹅", "鹅鹅鹅\t\n", "曲项向天歌", "白毛浮绿水", "红掌拨清波"]

# for poem_str in poem:
#     print("|%s|" % poem_str.strip().ljust(10, " "))

# poem = "\t\n咏鹅\t\n鹅鹅鹅\t\n曲项向天歌    白毛浮绿水 红掌拨清波"
# # print(poem)

# # print(poem.split())

# print(" ".join(poem.split()))


# def measure():
#     """ 测量温度和湿度 """
#     print('测量开始...')
#     temp = 39
#     wetness = 50
#     print('测量结束...')
#     # 元组，可以包含多个数据，可以使用元组让函数一次性返回多个值
#     # 如果函数返回的类型是元组，小括号可以省略
#     return (temp, wetness)


# # 使用多个变量接收结果时，变量的个数和元组的个数一定要相同
# result, _ = measure()
# print(result)

# def demo(num, num_list):
#     print("函数内部的代码")
#     # 在函数内部针对参数使用赋值语句，不会修改外部的实参变量
#     num = 100
#     num_list = [1, 2, 3]
#     print(num)
#     print(num_list)
#     print("函数执行完成")


# gl_num = 99
# gl_list = [4, 5, 6]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)


# def demo(num_list):
#     print("函数内部的代码")
#     num_list.append(9)
#     print(num_list)
#     print("函数执行完成")


# gl_list = [1, 2, 3]
# demo(gl_list)
# print(gl_list)


# def demo(num, num_list):
#     print("函数开始")
#     num += num
#     print(num)
#     num_list = num_list + num_list
#     # num_list += num_list
#     # num_list.extend(num_list)
#     print(num_list)
#     print("函数完成")


# gl_num = 9
# gl_list = [1, 3, 2]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)

# def sum_numbers(*args):
#     # def sum_numbers(args):
#     num = 0
#     for n in args:
#         num += n
#     # print(args)
#     return num


# result = sum_numbers(1, 2, 3, 4, 5)
# print(result)


# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)


# gl_nums = (1, 2, 3)
# gl_dict = {"name": "小明", "age": 18}
# demo(*gl_nums, **gl_dict)


# 递归
# def add_fuc(num):
#     if num == 1:
#         return 1
#     return num + add_fuc(num - 1)


# print(add_fuc(100))


# 递归的汉诺塔问题
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)


# move(9, "A", "B", "C")

class Cat():
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    # def __str__(self):
    #     return "我是小猫[%s]" % self.name

    # def eat(self):
    #     print("%s爱吃鱼" % self.name)

    # def drink(self):
    #     print("%s爱喝水" % self.name)


tom = Cat("tom")
print(tom)
# tom.eat()
# tom.drink()
del tom


# lazy_cat = Cat('lazy_cat')

# lazy_cat.drink()
# lazy_cat.eat()
