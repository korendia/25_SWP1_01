def multiply_digits(n):
    result_sequence = [n]
    while n >= 10:
        digits = [int(i) for i in str(n) if i != '0']
        product = 1
        for d in digits:
            product *= d
        result_sequence=product
        n = product
    if n<10:
        result_sequence=int(n)
    return result_sequence

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = multiply_digits(n)
        print(result)

        with open("text.txt","r") as f:
            t=(f.readline())