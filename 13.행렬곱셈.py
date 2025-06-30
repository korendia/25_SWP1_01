#Inhwan Bae,Kookmin University,2025, May,14

def make_matrix(row,col):#행렬생성파트
    matrix=[list(map(int,input().split()))for i in range(row)]
    return matrix

def mul_matrix(A,B):#행렬곱하여 새로운 행렬 만드는 파트
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range (len(B[0])):
            for k in range (len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        num = map(int, input().split())
        A_row = next(num)
        A_col = next(num)
        B_row = A_col
        B_col =next(num)
        A=make_matrix(A_row, A_col)
        B=make_matrix(B_row, B_col)
        C=mul_matrix(A,B)
        for row in C:#새로운 행렬 언패킹
            print(*row)
