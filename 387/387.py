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
from utils import miller_rabin, get_all_prime


prime_max = 1000000


def is_prime(n, primes):
    if n <= prime_max:
        return n in primes
    return miller_rabin(n)


def main():
    que = [(i, i) for i in range(1, 10)]
    cur = 0
    while cur < len(que):
        for i in range(10):
            num = que[cur][0] * 10 + i
            if num > 10 ** 14:
                continue
            dig_sum = que[cur][1] + i
            if num % dig_sum == 0:
                print(num)
                que.append((num, dig_sum))
        cur += 1
    # print(len(que))
    n = 10 ** 14
    res = 0
    primes = set(get_all_prime(prime_max))
    for item in que:
        if is_prime(item[0] // item[1], primes):
            for i in [1, 3, 7, 9]:
                if is_prime(item[0] * 10 + i, primes):
                    tem = item[0] * 10 + i
                    if tem >= n:
                        continue
                    print(tem)
                    res += tem
    print(res)


if __name__ == '__main__':
    main()
