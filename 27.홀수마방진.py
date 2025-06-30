#Inhwan Bae,Kookmin University,2025, August 5th
def magic_square(n):
    square=[[0 for i in range(n)] for j in range(n)]
    i,j = 0,n//2

    for count in range(1,n*n+1):
        square[i][j]=count
        next_i,next_j=(i-1)%n,(j+1)%n
        if square[next_i][next_j]:
            next_i,next_j=(i+1)%n,j
        i,j=next_i,next_j
    return square

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        num=int(input())
        square=magic_square(num)
        for j in square:
            print(*j)