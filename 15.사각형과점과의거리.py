def get_distances(x1, y1, x2, y2, x, y):
    if x1 <= x <= x2 and y1 <= y <= y2:
        return 0, 0

    nearest_x = min(max(x, x1), x2)
    nearest_y = min(max(y, y1), y2)

    dx = x - nearest_x
    dy = y - nearest_y
    d2 = dx * dx + dy * dy
    d1 = abs(dx) + abs(dy)

    return d2, d1


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        x, y = map(int, input().split())
        d2, d1 = get_distances(x1, y1, x2, y2, x, y)
        print(d2, d1)