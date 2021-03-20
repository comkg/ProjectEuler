# Copyright 2019 fssqawj Holding Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from utils import get_all_prime, quick_pow_mod
from tqdm import tqdm


cache = {0: 1, 1: 1, 2: 2}


def fac(n):
    if n in cache:
        # print(n, "hit")
        return cache[n]
    print(n)
    res = n * fac(n - 1)
    cache[n] = res
    return res


def calc(n):
    res = 0
    for i in range(5, 0, -1):
        print("find", n - i)
        res += fac(n - i)
    return res


def fac_mod(n, p):
    res = p - 1
    for i in range(p - 1, n, -1):
        res *= quick_pow_mod(i, p - 2, p)
        res %= p
    return res


def main():
    n = 10 ** 8
    primes = get_all_prime(n)
    res = 0
    for prime in tqdm(primes):
        if prime < 5:
            continue
        m_1 = prime - 1
        m_2 = 1
        m_5 = fac_mod(prime - 5, prime)
        m_4 = m_5 * (prime - 4) % prime
        m_3 = m_4 * (prime - 3) % prime
        res += (m_1 + m_2 + m_3 + m_4 + m_5) % prime
    print(res)


if __name__ == '__main__':
    main()
