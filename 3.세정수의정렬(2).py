t = int(input())

for i in range(1, t + 1):
    num = [int(c) for c in input().split(" ", 3)]

    a,b,c=num[0],num[1],num[2]

    if a<=b:
        if b<=c:
            print(a,b,c)
        else:
            if a<=c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if c<=b:
            print(c,b,a)
        else:
            if a<=c:
                print(b,a,c)
            else:
                print(b,c,a)