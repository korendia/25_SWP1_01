t = int(input())

for i in range(1, t + 1):
    count = int(input())
    num = [int(c) for c in input().split(" ", count - 1)]
    a = len(num)

    max_num = num[0]
    min_num = num[0]

    for b in range(a):
        if num[b] > max_num:
            max_num = num[b]
        if num[b] < min_num:
            min_num = num[b]

    print(str(max_num) + " " + str(min_num))