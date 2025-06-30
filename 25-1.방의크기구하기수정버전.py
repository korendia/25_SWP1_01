def room_count():
    t = int(input())

    for i in range(t):
        m, n = map(int, input().split())
        grid = [list(input().strip()) for i in range(n)]

        visited = [[False] * m for i in range(n)]
        room_sizes = []

        def dfs(r, c):
            count = 0
            stack = [(r, c)]
            visited[r][c] = True

            while stack:
                cur_r, cur_c = stack.pop()
                count += 1
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = cur_r + dr, cur_c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        if not visited[nr][nc] and grid[nr][nc] == '.':
                            visited[nr][nc] = True
                            stack.append((nr, nc))
            return count

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.' and not visited[i][j]:
                    room_size = dfs(i, j)
                    room_sizes.append(room_size)

        room_sizes.sort(reverse=True)
        print(len(room_sizes))
        print(" ".join(map(str, room_sizes)))


if __name__ == "__main__":
    room_count()