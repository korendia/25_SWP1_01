#Inhwan Bae,Kookmin University,2025, April,15

def isMultipleOf(k):
    def sumOfDigits(num):
        sum = 0
        for d in num:
            sum += ord(d) - ord('0')
        return sum

    def isMultipleOf2(num):
        return (ord(num[-1]) - ord('0')) % 2 == 0

    def isMultipleOf3(num):
        return sumOfDigits(num) % 3 == 0

    def isMultipleOf4(num):
        return int(num[-2:]) % 4 == 0 if len(num) >= 2 else int(num) % 4 == 0

    def isMultipleOf5(num):
        return num[-1] in ('0','5')

    def isMultipleOf6(num):
        return ((ord(num[-1]) - ord('0')) % 2 == 0) and (sumOfDigits(num) % 3 == 0)

    def isMultipleOf7(num):
        while len(num) > 1:
            if len(num) < 2:
                break
            a = int(num[0])
            b = int(num[1])
            replaced = str(a * 3 + b)
            num = replaced + num[2:]
        return num == '7'

    def isMultipleOf8(num):
        return int(num[-3:]) % 8 == 0 if len(num) >= 3 else int(num) % 8 == 0

    def isMultipleOf9(num):
        return sumOfDigits(num) % 9 == 0

    def isMultipleOf10(num):
        return int(num[-1]) == 0

    def isMultipleOf11(num):
        count_even = 0
        count_odd = 0
        for i in range(len(num)):
            digit = int(num[i])
            if i % 2 == 0:
                count_even += digit
            else:
                count_odd += digit
        return abs(count_even - count_odd) % 11 == 0

    fnMultipleOf = [None, None, isMultipleOf2, isMultipleOf3, isMultipleOf4,
                    isMultipleOf5, isMultipleOf6, isMultipleOf7, isMultipleOf8,
                    isMultipleOf9, isMultipleOf10, isMultipleOf11]

    return fnMultipleOf[k]

if __name__ == "__main__":
    T=int(input())
    for i in range(T):
        num=input()
        print(" ".join(str(int(isMultipleOf(k)(num))) for k in range(2, 12)))