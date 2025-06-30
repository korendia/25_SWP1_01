def count_zero():
    nums = list(map(int, input().split()))
    count_2 = 0
    count_5 = 0
    real_nums=nums[1:]
    product=1

    for num in real_nums:
        product *= num
        while num % 2 == 0 and num > 0:
            count_2 += 1
            num //= 2
        while num % 5 == 0 and num > 0:
            count_5 += 1
            num //= 5

    zero_num=min(count_2,count_5)
    last_num=(product//(10**(zero_num)))%10

    return print(last_num,zero_num)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        count_zero()