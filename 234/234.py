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
import math

from utils import get_all_prime


def calc(a, b, c):
    if a > b or b < c:
        return 0
    start = a + (c - (a % c)) % c
    remain = b - start - 1
    cnt = remain // c + 1
    return start * cnt + (cnt - 1) * cnt // 2 * c


def main():
    n = 999966663333
    # n = 1000
    primes = get_all_prime(int(math.sqrt(n) + 100))
    res = 0
    for i in range(len(primes) - 1):
        lower = primes[i] * primes[i] + 1
        upper = primes[i + 1] * primes[i + 1]
        if lower > n:
            continue
        if upper > n:
            upper = n + 1
        res += calc(lower, upper, primes[i])
        res += calc(lower, upper, primes[i + 1])
        res -= 2 * calc(lower, upper, primes[i] * primes[i + 1])
    print(res)


if __name__ == '__main__':
    main()
    # print(calc(33, 45, 3))
