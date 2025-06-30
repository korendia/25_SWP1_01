def zigzag(n, k):
    start = (k - 1) * k // 2 + 1
    num = list(range(start, start + k))
    if k % 2 == 0:
        num.reverse()
    return "*".join(map(str, num))

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, k = map(int, input().split())
        print(zigzag(n, k))

