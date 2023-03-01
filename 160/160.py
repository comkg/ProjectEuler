from tqdm import tqdm
from multiprocessing import Pool


def calc(start, end, mod):
    res = 1
    for i in tqdm(range(start, end)):
        res *= i
        while res % 10 == 0:
            res //= 10
        res %= mod
    return res


def main():
    n = 10 ** 12
    mod = 10000000000

    res = []
    pool_cnt = 46
    with Pool(processes=pool_cnt) as pool:
        for i in range(pool_cnt + 1):
            start = 1 if i == 0 else i * (n // pool_cnt)
            end = min((i + 1) * (n // pool_cnt), n + 1)
            res.append(pool.apply_async(calc, (start, end, mod)))
        pool.close()
        pool.join()
        ans = 1
        for item in res:
            ans *= item.get()
            while ans % 10 == 0:
                ans //= 10
            ans %= mod
        print(ans)


if __name__ == "__main__":
    main()


# 81883416576
