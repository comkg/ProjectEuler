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
from utils import get_all_prime
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


def main():
    n = 10 ** 6
    primes = get_all_prime(n)
    res = 0
    for prime in tqdm(primes):
        if prime < 5:
            continue
        res += calc(prime) % prime
    print(res)


if __name__ == '__main__':
    main()
