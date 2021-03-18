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


def find_prev(n, k):
    cur_cnt = (k >> (n << 1)) & 3
    if cur_cnt == 0:
        return None
    return k - (cur_cnt << (n << 1)) + ((cur_cnt - 1) << (n << 1))


def count_one(n):
    res = 0
    while n > 0:
        res += n & 3
        n >>= 2
    return res


def summary(k):
    for i in range(10):
        if k & 3 != 0:
            print(i, k & 3, end=", ")
        k >>= 2
    print()


def main():
    n = 18
    dp = [[0 for _ in range(1 << 20)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, 10):
        dp[1][1 << (i << 1)] = 1
    for i in tqdm(range(2, n + 1)):
        for j in range(10):
            for k in range(1 << 20):
                prev = find_prev(j, k)
                if prev is None:
                    continue
                dp[i][k] += dp[i - 1][prev]
    res = 0
    # print(dp[1][4], dp[2][8])
    for i in range(1 << 20):
        if count_one(i) == n:
            # if dp[n][i] > 0:
            #     summary(i)
            #     print(dp[n][i])
            res += dp[n][i]
    print(res)


if __name__ == '__main__':
    main()
    # print(8 & 3)
    # print(count_one(8))
    # print(find_prev(9, 1 << 19))
