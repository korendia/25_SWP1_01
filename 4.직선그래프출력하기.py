#Inhwan Bae,Kookmin University,2025, May,3

def picture(num):   #실제 출력될 그림 작성
    center_num=(num//2)   #K값의 중간값을 가리키는 오프셋 확인
    common_list=['.']*num   #x축 위아래 작성
    common_list[center_num]='I'
    center_list=['+']*num   #x축 작성
    center_list[center_num]='O'
    for i in range(num):
        if i != center_num:
            common_list[-(i+1)]='*'
            print(str(''.join(common_list)))
            common_list=['.']*num
            common_list[center_num] = 'I'
        else:
            print(''.join(center_list))

def count_num():    #출력할 횟수 확인
    for i in range(T):
        K=input()
        list_num.append(K)
    return list_num

if __name__ == '__main__':
    T = int(input())
    list_num = []
    count_num()
    for i in range(T):
        picture(int(list_num[i]))