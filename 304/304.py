from utils import fibonacci, miller_rabin, is_prime
from tqdm import tqdm


def main():
    mod = 1234567891011
    n = 10 ** 14
    num = 100000
    res = 0
    for i in range(30):
        print(i, fibonacci(i, mod))
    last = fibonacci(n - 1, mod)
    current = fibonacci(n, mod)
    print(last, current)
    for i in tqdm(range(num)):
        # print(i + 1, miller_rabin(i + 1), is_prime(i + 1))
        while True:
            n += 1
            nex = (last + current) % mod
            last = current
            current = nex
            if miller_rabin(n):
                break

        res += current
        res %= mod

    print(res)


if __name__ == "__main__":
    main()
