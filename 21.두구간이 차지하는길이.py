#Inhwan Bae,Kookmin University,2025, May,25
#3차 수정본-최적화본

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())

        # 겹치는 구간 계산
        overlap_start = max(a, c)
        overlap_end = min(b, d)
        overlap = max(0, overlap_end - overlap_start)

        # 전체 길이 계산
        if b < c or d < a:
            total = (b - a) + (d - c)
        else:
            total = max(b, d) - min(a, c)

        print(overlap,total)