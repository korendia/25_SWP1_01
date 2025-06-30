def simulate_life(n, k, cells):
    for _ in range(k):
        next_cells = cells[:]
        for i in range(n):
            if i == 0:
                neighbors = cells[1]
            elif i == n - 1:
                neighbors = cells[n - 2]
            else:
                neighbors = cells[i - 1] + cells[i + 1]

            if neighbors < 3 or neighbors > 7:
                if cells[i] > 0:
                    next_cells[i] -= 1
            elif 4 <= neighbors <= 7:
                if cells[i] < 9:
                    next_cells[i] += 1

        cells = next_cells
    return cells

# 입력 처리
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        cells = list(map(int, input().split()))
        result = simulate_life(n, k, cells)
        print(*result)