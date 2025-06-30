def count_digit(n):
    new_num=n.strip('0')
    count_num=len(new_num)
    count=0
    only_num=set(new_num)
    for i in range(count_num):
        if int(new_num)%int(only_num[i])==0:
            count+=1
    return count

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        print(count_digit(input()))