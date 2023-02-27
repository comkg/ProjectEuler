from utils import is_square
from tqdm import tqdm


cache = {}


def calc(x, y):
    '''
    y / x
    0: y,
    1: y - y / x * 1
    2: y - y / x * 2
    ...
    x - 1: y - y / x * (x - 1)
    x: 0
    '''
    global cache
    key = str(x) + "-" + str(y)
    rev_key = str(y) + "-" + str(x)
    if key in cache:
        return cache[key]
    if rev_key in cache:
        return cache[rev_key]
    res = 0
    for i in range(1, x):
        res += int(y - y / x * i - 1e-9)
    cache[key] = res
    cache[rev_key] = res
    return res


def main():
    n = 100
    tot = 0
    ans = 0
    for a in tqdm(range(1, n + 1)):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    res = calc(a, b) + calc(c, b) + calc(a, d) + calc(c, d)
                    res += (a + b + c + d - 3)
                    if is_square(res):
                        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
