#Inhwan Bae,Kookmin University,2025, May,4

def print_hourglass(size):
    center = size//2
    for i in range(size):
        if i <= center:
            offset=i
        else:
            offset=size-1-i

        count = size-offset*2
        print('-'*offset+''.join('*' if j%2==0 else '+' for j in range(count))+'-'*offset)

case_cnt = int(input())

while case_cnt > 0:
    hourglass_size = int(input())
    print_hourglass(hourglass_size)
    case_cnt -= 1