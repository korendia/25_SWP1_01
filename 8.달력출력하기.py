def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(year, month):
    month_days = [31, 28 + is_leap(year), 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
    return month_days[month - 1]


def count_days_since_1582(y, m):
    total_days = 0
    for year in range(1582, y):
        total_days += 365 + is_leap(year)
    for month in range(1, m):
        total_days += get_days_in_month(y, month)
    return total_days


def print_calendar(y, m):
    print(f"{y} {m}")

    first_day = (5 + count_days_since_1582(y, m)) % 7
    days_in_month = get_days_in_month(y, m)

    weeks = []
    week = []

    # 첫 주: 첫째날 이전은 0
    for _ in range(first_day):
        week.append(0)

    day = 1
    while day <= days_in_month:
        week.append(day)
        day += 1
        if len(week) == 7:
            weeks.append(week)
            week = []

    # 마지막 주 남은 칸은 0으로 채우기
    if week:
        while len(week) < 7:
            week.append(0)
        weeks.append(week)

    # 출력
    for week in weeks:
        print(' '.join(str(d) for d in week))


def main():
    with open("input.txt", "r") as f:
        t = int(f.readline())
        for _ in range(t):
            y, m = map(int, f.readline().split())
            print_calendar(y, m)


if __name__ == '__main__':
    main()