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
from tqdm import tqdm

from utils import quick_pow_mod, gcd


def g(n):
    res = 1
    for i in range(1, n):
        if gcd(i, n) == 1:
            print(n, i)
            res *= i
    return res


def _find(n, factors):
    res = n

    def _num_ones(x):
        ones = 0
        mul = 1
        cur = 0
        while x > 0:
            if x & 1:
                mul *= factors[cur]
                ones += 1
            x >>= 1
            cur += 1
        return ones, mul

    for i in range(1, 1 << len(factors)):
        ones, mul = _num_ones(i)
        if ones & 1:
            res -= n // mul
        else:
            res += n // mul

    return res


def find(a, b, factors):
    return _find(b - a, factors)


def main():
    n = 10
    mod = 1000000007
    res = 1

    print(find(9, 10, [3]))

    prime_factors = {}
    for i in tqdm(range(2, n, 1)):
        if i not in prime_factors:
            for j in range(i, n, i):
                if j not in prime_factors:
                    prime_factors[j] = []
                prime_factors[j].append(i)
    # print(prime_factors)

    for i in tqdm(range(2, n, 1)):
        cnt = find(i, n, prime_factors[i])
        res = (res * quick_pow_mod(i, cnt, mod)) % mod

    print(res)
    # res = 1
    # for i in range(1, 11):
    #     # print(i, g(i))
    #     res *= g(i)
    # print(res, res % mod)


if __name__ == '__main__':
    # may relate to problem 193
    main()
