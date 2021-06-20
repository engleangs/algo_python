def solve(x, coins=[]):
    if x < 0:
        return float("+inf")
    if x == 0:
        return 0
    best = float("+inf")
    for c in coins:
        best = min(best, solve(x - c, coins) + 1)
    return best


ready = {}


def solve_v2(x, coins=[]):
    if x < 0:
        return float("+inf")
    if x == 0:
        return 0
    if x in ready:
        return ready[x]
    best = float("+inf")
    for c in coins:
        best = min(best, solve_v2(x - c, coins) + 1)
        ready[x] = best
    return best


def solve_v3(x, coins=[]):
    values = [0 for _ in range(0, x + 1)]
    for i in range(1, x + 1):
        values[i] = float("+inf")
        for c in coins:
            if x - c >= 0:
                values[i] = min(values[i], values[c - i] + 1)
    return values[x]


if __name__ == "__main__":
    coins = [1, 2, 3, 5]
    x = 10
    print("solve for ", x, " : ", solve(x, coins))
    print("solve for v2 : ", x, ": ", solve_v2(x, coins))
