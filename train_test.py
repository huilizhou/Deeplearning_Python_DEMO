import os
import random


def rand_index_list(start=0, end=9, proportion=1):
    rand_index_list = []
    while len(rand_index_list) < proportion * 10:
        rand_index = random.randint(start, end)
        if rand_index not in rand_index_list:
            rand_index_list.append(rand_index)
    rand_index_list.sort()
    return rand_index_list


def rand_serial(train_proportion):
    rand_train_index_list = rand_index_list(proportion=train_proportion)
    return rand_train_index_list


def find_rand_file(path_fold=None):
    rand_train_index_list = []
    xml_list = []
    for _, _, files in os.walk(path_fold):
        for f in files:
            if os.path.splitext(f)[-1] == ".xml":
                xml_list.append(os.path.splitext(f)[-2])
    # print(xml_list)
    index_list_num = len(xml_list) // 10

    for index in range(index_list_num):
        train_index_list = rand_serial(0.8)

        rand_train_index_list = rand_train_index_list + \
            [x + 10 * index for x in train_index_list]

    train_list = [xml_list[i] for i in rand_train_index_list]
    test_list = [x for x in xml_list if x not in train_list]

    return train_list, test_list


def write_file(voc_path):
    train_list, test_list = find_rand_file(voc_path)
    with open(voc_path + "/train.txt", 'w') as f_w:
        for x in train_list:
            f_w.write(x)
            f_w.write("\n")
    with open(voc_path + "/test.txt", 'w') as f_w:
        for x in test_list:
            f_w.write(x)
            f_w.write("\n")


if __name__ == "__main__":
    write_file("I:\TESTT\DECT")
