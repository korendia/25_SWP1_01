#Inhwan Bae,Kookmin University,2025, May,27

def self_hamming(num):
    return num.count('1')


def hamming():
    first_num,second_num=map(int,input().split())
    first_num=str(bin(first_num)[2:])
    second_num=str(bin(second_num)[2:])
    time=max(len(first_num),len(second_num))
    first_num=first_num.zfill(time)
    second_num=second_num.zfill(time)

    f_hamming=self_hamming(first_num)
    s_hamming=self_hamming(second_num)
    count = 0

    for i in range (time):
        if first_num[i]!=second_num[i]:
            count+=1

    print(f_hamming,s_hamming,count)


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        hamming()