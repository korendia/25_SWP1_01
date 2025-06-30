#Inhwan Bae,Kookmin University,2025, May,15
#3차 작성본-최적화본

def mul_matrix(A, B):
    #이중 리스트 컴프리헨션 사용
    #내부의 A_row,A_col,B_col은 스코프 우선순위로 인하여 메인함수의 지역변수와 별개처리됨
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)]for A_row in A]

if __name__ == '__main__':
    for i in range(int(input())):
        A_row, A_col, B_col = map(int, input().split())
        A = [list(map(int, input().split())) for i in range(A_row)]
        B = [list(map(int, input().split())) for i in range(A_col)]  # A_col == B_row
        C = mul_matrix(A, B)
        for row in C:
            print(*row)

