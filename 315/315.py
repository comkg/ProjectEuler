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


dig_map = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 4, 8: 7, 9: 6}

overlap_lap = {0: [6, 2, 4, 4, 3, 4, 5, 4, 6, 5],
               1: [2, 2, 1, 2, 2, 1, 1, 2, 2, 2],
               2: [4, 1, 5, 4, 2, 3, 4, 2, 5, 4],
               3: [4, 2, 4, 5, 3, 4, 4, 3, 5, 5],
               4: [3, 2, 2, 3, 4, 3, 3, 3, 4, 4],
               5: [4, 1, 3, 4, 3, 5, 5, 3, 5, 5],
               6: [5, 1, 4, 4, 3, 5, 6, 3, 6, 5],
               7: [4, 2, 2, 3, 3, 3, 3, 4, 4, 4],
               8: [6, 2, 5, 5, 4, 5, 6, 4, 8, 6],
               9: [5, 2, 4, 5, 4, 5, 5, 4, 6, 6]}


def get_dig_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def get_steps(n):
    res = [n]
    while n > 9:
        n = get_dig_sum(n)
        res.append(n)
    return res


def get_num_cnt(n):
    res = 0
    while n > 0:
        res += dig_map[n % 10]
        n //= 10
    return res


def get_normal_cnt(x):
    res = 0
    for i in x:
        tem = get_num_cnt(i)
        res += 2 * tem
    return res


def get_overlap_cnt(x, y):
    res = 0
    while x > 0 and y > 0:
        t_x = x % 10
        t_y = y % 10
        res += overlap_lap[t_x][t_y]
        x //= 10
        y //= 10
    return res


def get_smart_cnt(x):
    res = 0
    remain = 0
    for idx, num in enumerate(x):
        tem = get_num_cnt(num)
        res += (tem - remain)
        if idx < len(x) - 1:
            remain = get_overlap_cnt(num, x[idx + 1])
        else:
            remain = 0
        res += (tem - remain)
    return res


def main():
    n = 2 * 10 ** 7
    primes = get_all_prime(n)
    res = 0
    for prime in primes:
        if prime < n // 2:
            continue
        steps = get_steps(prime)
        res += (get_normal_cnt(steps) - get_smart_cnt(steps))
    print(res)


if __name__ == '__main__':
    main()
    # for i in range(10):
    #     for j in range(10):
    #         assert overlap_lap[i][j] == overlap_lap[j][i], f"{i}-{j}"
    # print(get_num_cnt(11))
    # print(get_smart_cnt(get_steps(137)))
