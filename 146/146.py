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
import random

from utils import get_all_prime, quick_pow_mod


def is_prime(n, primes):
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True


def miller_rabin(n):
    d = n - 1
    i = random.randint(1, n-1)
    while d != 1:
        if quick_pow_mod(i, d, n) == 1:
            if d % 2 != 0:
                return True
            d = d // 2
            if quick_pow_mod(i, d, n) == n - 1:
                return True
        else:
            return False
    return True


def satisfy(n):
    target = [1, 3, 7, 9, 13, 27]
    res = []
    for i in [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27]:
        # if is_prime(n * n + i, primes):
        if miller_rabin(n * n + i):
            res.append(i)
    return target == res


def main():
    # 1, 3, 7, 9, 13, 27
    n = 150000000
    # all_primes = get_all_prime(n)
    res = 0
    for i in tqdm(range(10, n, 10)):
        if satisfy(i):
            res += i
            print(i)
    print(res)


if __name__ == '__main__':
    main()
