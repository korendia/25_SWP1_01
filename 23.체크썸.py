def cs(n):
    n=bin(n)[2:].zfill(32)
    n_s=int(n[0:8],2)+int(n[8:16],2)+int(n[16:24],2)
    n_s %= 256
    if (255-n_s)==int(n[24:32],2):
        return 1
    else:
        return 0
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        print(cs(int(input())))