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

from utils import get_all_prime


def count(n, m):
    res = 0
    while n > 0:
        res += n // m
        n //= m
    return res


def satisfy(n, prime, cnt):
    lower, upper = 2, n
    res = -1
    while lower <= upper:
        mid = (lower + upper) // 2
        if count(mid, prime) >= cnt:
            upper = mid - 1
            res = mid
        else:
            lower = mid + 1
    return res


def find(items):
    res = 0
    for prime in items:
        cnt = items[prime]
        res = max(res, satisfy(prime * cnt, prime, cnt))
    return res


def filter_prime(n, res):
    for i in tqdm(range(2, n + 1, 1)):
        if i not in res:
            for j in range(i, n + 1, i):
                if j not in res:
                    res[j] = {}
                cnt = 0
                tem_j = j
                while tem_j % i == 0:
                    cnt += 1
                    tem_j //= i
                res[j][i] = cnt
    return res


def main():
    n = 10 ** 8
    primes = {}
    filter_prime(n, primes)
    print(primes)
    res = 0
    for i in tqdm(range(2, n + 1, 1)):
        # print(i, find(i, primes))
        res += find(primes[i])
    print(res)


if __name__ == '__main__':
    main()
    # print(satisfy(12, 3, 4))
