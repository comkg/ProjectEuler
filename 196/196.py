from tqdm import tqdm
from utils import miller_rabin, is_prime


def neighbours(n, x, p_l, p_r, n_l):
    res = []
    if x - n >= p_l:
        res.append(x - n)
    if x - n + 1 <= p_r:
        res.append(x - n + 1)
    if x - n + 2 <= p_r:
        res.append(x - n + 2)
    if x + n - 1 >= n_l:
        res.append(x + n - 1)
    res.append(x + n)
    res.append(x + n + 1)
    return res


def calc(i, items, cache, hit, l, n_1_l):
    res = 0
    cnt = 0
    for item in items:
        if cache[item]:
            cnt += 1
    if cnt < 2:
        return res
    # print(i, items)
    if i not in hit and l <= i < n_1_l:
        res += i
        hit.add(i)
    for item in items:
        if cache[item] and l <= item < n_1_l and item not in hit:
            res += item
            # print(item)
            hit.add(item)
    return res


def main():
    for i in range(15):
        f = i * (i - 1) // 2 + 1
        print(i, " ".join([str(x) for x in range(f, f + i)]))
    cache = {}
    n = 7208785
    first = (n - 2) * (n - 3) // 2 + 1
    last = (n + 3) * (n + 2) // 2 + 1
    for i in tqdm(range(first, last)):
        cache[i] = miller_rabin(i)

    res = 0
    hit = set()
    p_2_l = (n - 2) * (n - 3) // 2 + 1
    p_1_l = (n - 1) * (n - 2) // 2 + 1
    l = n * (n - 1) // 2 + 1
    n_1_l = (n + 1) * n // 2 + 1
    n_2_l = (n + 2) * (n + 1) // 2 + 1

    for i in range(p_1_l, l):
        if not cache[i]:
            continue
        items = neighbours(n - 1, i, p_2_l, p_1_l - 1, l)
        res += calc(i, items, cache, hit, l, n_1_l)

    for i in range(l, n_1_l):
        if not cache[i]:
            continue
        items = neighbours(n, i, p_1_l, l - 1, n_1_l)
        res += calc(i, items, cache, hit, l, n_1_l)

    for i in range(n_1_l, n_2_l):
        if not cache[i]:
            continue
        items = neighbours(n + 1, i, l, n_1_l - 1, n_2_l)
        res += calc(i, items, cache, hit, l, n_1_l)

    print(res)


if __name__ == "__main__":
    main()

# 5678027: 79697256800321526
# 7208785: 242605983970758409



