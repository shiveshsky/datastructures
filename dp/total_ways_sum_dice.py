def total_ways(d=3, f=6, s=12):
    if s == 0 and d == 0:
        return 1
    if s < 0 or d == 0:
        return 0
    ways = 0
    for fa in range(1, f + 1):
        ways += total_ways(d - 1, f, s - fa)
    return ways


if __name__ == '__main__':
    print(total_ways())
