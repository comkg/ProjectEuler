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
from tqdm import tqdm

from utils import is_square


def fac_square_sum(n):
    res = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res += i * i
            if i * i != n:
                res += (n // i) * (n // i)
    return res


def prime_split(n, res):
    for i in range(1, n):
        res[i] = []
    for i in tqdm(range(2, n)):
        if len(res[i]) == 0:
            for j in range(i, n, i):
                tem = 0
                tem_j = j
                while tem_j % i == 0:
                    tem += 1
                    tem_j //= i
                res[j].append((i, tem))
    return res


def calc_square_sum(item):
    res = 1
    for x in item:
        tem = 1
        cur_p = x[0] * x[0]
        for j in range(x[1]):
            tem += cur_p
            cur_p = cur_p * x[0] * x[0]
        res *= tem
    return res


def main():
    n = 64000000
    prime_res = prime_split(n, {})
    # print(prime_res)
    res = 1
    for i in tqdm(range(2, n)):
        if is_square(calc_square_sum(prime_res[i])):
            print(i)
            res += i
        # if is_square(fac_square_sum(i)):
        #     print(i, "true")
    print(res)


if __name__ == '__main__':
    # print(fac_square_sum(42))
    main()
    # print(calc_square_sum([(2, 1), (5, 1)]))
