def centerhigh():
    num=map(int,input().split())
    center_num=0
    past=next(num)
    present=next(num)
    first=False

    for future in num:
        if past<present:
            first=True
        if first==True:
            if past <= present > future:
                center_num += 1
                first=False
        past, present = present, future
    return center_num

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        print(centerhigh())