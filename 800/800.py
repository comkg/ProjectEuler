from utils import get_all_prime
import math
from tqdm import tqdm


def main():
    n = 800800
    target = n ** n
    log_2 = int(math.log2(target))
    primes = get_all_prime(log_2)
    # print(primes)
    l_t = math.log2(target)
    res = 0
    l = 0
    r = len(primes) - 1
    while l < r:
        print(l, r)
        while primes[r] * math.log2(primes[l]) + primes[l] * math.log2(primes[r]) > l_t:
            r -= 1
        res += (r - l)
        # print(l, r)
        l += 1

    print(res)


if __name__ == "__main__":
    main()
