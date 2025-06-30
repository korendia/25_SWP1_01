#Inhwan Bae,Kookmin University,2025, May,13

def make_matrix(row,col):#행렬생성파트
    matrix=[list(map(int,input().split()))for i in range(row)]
    return matrix

def add_matrix(A,B):#행렬더하여 새로운 행렬 만드는 파트
    row=len(A)
    col=len(A[0])
    C=[[A[i][j]+B[i][j]for j in range(col)]for i in range(row)]
    return C

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        num = map(int, input().split())
        row = next(num)
        col = next(num)
        A=make_matrix(row, col)
        B=make_matrix(row, col)
        C=add_matrix(A,B)
        for row in C:#새로운 행렬 언패킹
            print(*row)
