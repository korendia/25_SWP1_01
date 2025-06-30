def get_area(px, py, qx, qy):
    return (qx - px) * (qy - py)


def get_intersection_area(p1, q1, p2, q2):
    ix1 = max(p1[0], p2[0])
    iy1 = max(p1[1], p2[1])
    ix2 = min(q1[0], q2[0])
    iy2 = min(q1[1], q2[1])

    if ix1 < ix2 and iy1 < iy2:
        return (ix2 - ix1) * (iy2 - iy1)
    else:
        return 0


def get_bounding_perimeter(p1, q1, p2, q2):
    min_x = min(p1[0], p2[0])
    max_x = max(q1[0], q2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(q1[1], q2[1])
    return 2 * ((max_x - min_x) + (max_y - min_y))


def solve_case(p1, q1, p2, q2):
    area1 = get_area(*p1, *q1)
    area2 = get_area(*p2, *q2)
    overlap = get_intersection_area(p1, q1, p2, q2)
    total_area = area1 + area2 - overlap

    if overlap > 0:
        perimeter = get_bounding_perimeter(p1, q1, p2, q2)
    else:
        perimeter = 2 * ((q1[0] - p1[0]) + (q1[1] - p1[1])) + 2 * ((q2[0] - p2[0]) + (q2[1] - p2[1]))

    return total_area, perimeter


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        px1, py1, qx1, qy1 = map(int, input().split())
        px2, py2, qx2, qy2 = map(int, input().split())

        p1, q1 = (px1, py1), (qx1, qy1)
        p2, q2 = (px2, py2), (qx2, qy2)

        area, perimeter = solve_case(p1, q1, p2, q2)
        print(area,perimeter)