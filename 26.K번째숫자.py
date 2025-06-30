def count_num(n):
    k_num = ''
    count = 1
    while len(k_num) <= n:
        k_num += str(count)
        count += 1
    return k_num[n - 1]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        num = int(input())
        print(count_num(num))

