'''
扩展生成500个txt
取224*224=50176行
相当于224*224*9

'''
import random


def copyfile(dstfile, linenum):
    """
        get linenum different lines out from srcfile at random
        and write them into dstfile
    """
    result = []
    ret = False
    try:
        srcfd = open('original.txt', 'r')
    except IOError:
        print('srcfile doesnot exist!')
        return ret
    try:
        dstfd = open(dstfile, 'w')
    except IOError:
        print('dstfile doesnot exist!')
        return ret
    srclines = srcfd.readlines()
    srclen = len(srclines)
    while len(set(result)) < int(linenum):
        s = random.randint(0, srclen - 1)
        result.append(srclines[s])
    for content in set(result):
        dstfd.write(content)
    srcfd.close()
    dstfd.close()
    ret = True
    return ret


if __name__ == "__main__":
    # srcpath = input('input srcfile path')
    # dstpath = input('input dstfile path')
    # linenum = input('input linenum')
    i = 1
    while i <= 500:
        dstpath = str(i) + '.txt'
        linenum = 50176
        print(copyfile(dstpath, linenum))
        i += 1
