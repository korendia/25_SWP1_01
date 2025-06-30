def double_num(num):
    new_num=bin(num)[2:]
    num_1=new_num.count('1')
    num_0=new_num.count('0')
    print(num_0,num_1)

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        t = int(f.readline())
        for i in range(t):
            num=int(f.readline().strip())
            double_num(num)


