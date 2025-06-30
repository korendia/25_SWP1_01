t = int(input())

for i in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = map(int,input().split())

    s = (x2-x1)*(y2-y1) + (x4-x3)*(y4-y3)

    if max(x2, x4) - min(x1, x3) < (x2-x1) + (x4-x3) and max(y2, y4) - min(y1, y3) < (y2-y1) + (y4-y3) :
        set_x = [x1,x2,x3,x4]
        set_y = [y1,y2,y3,y4]
        set_x.sort()
        set_y.sort()

        print(s - (set_x[2]-set_x[1])*(set_y[2]-set_y[1]),(max(x2, x4) - min(x1, x3))*2 + (max(y2, y4) - min(y1, y3))*2)

    else:
        print(s,(y4-y3+y2-y1+x4-x3+x2-x1)*2)