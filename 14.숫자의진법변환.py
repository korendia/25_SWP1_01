#Inhwan Bae,Kookmin University,2025, May,15

def formation():
    base_formation,num,new_formation=input().split()
    base_formation=int(base_formation)
    new_formation=int(new_formation)

    new_num=int(str(num),base_formation)
    digits='0123456789abcdefg'
    result=""

    while new_num>0:
        result=digits[new_num%new_formation]+result
        new_num//=new_formation

    return result

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        print(formation())