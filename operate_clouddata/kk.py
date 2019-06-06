# encoding=utf-8
import random


def copyfile(srcfile, dstfile, linenum):
    """
        get linenum different lines out from srcfile at random
        and write them into dstfile
    """
    result = []
    ret = False
    try:
        srcfd = open(srcfile, 'r')
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

    srcpath = '1.txt'
    dstpath = '2.txt'
    linenum = 2
    print(copyfile(srcpath, dstpath, linenum))
