# 你的源文件用了模块化的思想，很不错，
# 但在我的电脑上生成一个50176行的文件要334s，
# 更何况是500个文件，（下面的代码一个文件只需0.1s）
# 所以，尤其是在数据分析和处理中，
# 模块化和效率同等重要，可能效率更重要一些，
# 因为数据分析更注重算法，编程技法次之，
# 要注意噢~~
import numpy as np

with open('banana0.txt', 'r') as ori_file:
    ori_content = ori_file.readlines()
max_length = len(ori_content)
line_num = 50176

for i in range(500):
    print(i + 1)
    random_indice = np.random.choice(max_length, line_num)
    result = [ori_content[index] for index in random_indice]
    with open(str(i + 1) + ".txt", 'w') as des_file:
        des_file.writelines(result)
