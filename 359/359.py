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


def find(n):
    x = int(math.sqrt(2 * n)) + 1
    return x * x - n


def next_sqs(n):
    res = []
    for i in range(int(math.sqrt(n)) + 1, int(math.sqrt(2 * n)) + 1):
        res.append(i * i)
    return res


def find_fir(limit):
    cur = 1
    res = []
    while cur < limit:
        nxt_sqs = next_sqs(cur)
        flag = False
        for nxt_sq in nxt_sqs:
            pre = nxt_sq - cur
            if pre < cur and find(pre) == cur:
                flag = True
                break
        if not flag:
            res.append(cur)
        cur += 1
    return res


def get_factors(x):
    res = []
    for i in tqdm(range(1, int(math.sqrt(x + 1)) + 1)):
        if x % i == 0:
            res.append(i)
    return res


def calc(i, j):
    if i == 1:
        a = 2
        fir = 1
    elif i % 2 == 1:
        a = i
        idx = i // 2
        fir = 2 * idx * idx + 2 * idx
    else:
        a = i + 1
        idx = i // 2
        p_idx = idx - 1
        fir = (idx * idx + idx) + (p_idx * p_idx + p_idx)
    if j % 2 == 1:
        return fir + (j - 1) // 2 * (j + 2 * a - 2)
    return (a + j - 2) * (a + j - 2) - fir - (j - 2) // 2 * (j + 2 * a - 3)


def main():
    # limit = 1000
    n = 71328803586048
    # firs = find_fir(limit)
    factors = get_factors(n)
    print(factors)
    # print(firs)
    # res = set()
    # for fir in firs:
    #     cnt = 0
    #     cur = fir
    #     while cnt < 100:
    #         print(cur, end=", ")
    #         cur = find(cur)
    #         cnt += 1
    #     print()
    # print(calc(99, 100))
    res = 0
    for factor in factors:
        res += calc(factor, n // factor)
        res += calc(n // factor, factor)
    print(res)


if __name__ == '__main__':
    main()
