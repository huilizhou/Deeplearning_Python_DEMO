result = []
with open('original.txt', 'r') as f:
    for line in f:
        result.append(list(map(float, line.split(' '))))
    print(result)
