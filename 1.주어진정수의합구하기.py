t=int(input())
count=0

for i in range(1,t+1):
    count=int(input())
    num=[int(c) for c in input().split(" ",count-1)]
    sumnum=0
    for data in num:
        sumnum += data

    print((sumnum))