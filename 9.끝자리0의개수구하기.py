def count_zero():
    nums = list(map(int, input().split()))
    count_2 = 0
    count_5 = 0
    real_nums=nums[1:]

    for num in real_nums:
        while num % 2 == 0 and num > 0:
            count_2 += 1
            num //= 2
        while num % 5 == 0 and num > 0:
            count_5 += 1
            num //= 5

    return min(count_2, count_5)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(count_zero())