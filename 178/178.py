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


def summary(n):
    res = []
    cur = 0
    while n > 0:
        if n & 1:
            res.append(cur)
        n >>= 1
        cur += 1
    return res


def main():
    n = 40
    dp = [[[0 for _ in range(1 << 10)] for _ in range(10)]
          for _ in range(n + 1)]
    for i in range(1, 10):
        dp[1][i][1 << i] = 1
    for i in range(2, n + 1):
        for j in range(10):
            for k in range(1 << 10):
                if (k >> j) & 1 == 0:
                    continue
                if j == 0:
                    dp[i][j][k] = dp[i - 1][j + 1][k] \
                                  + dp[i - 1][j + 1][k - (1 << j)]
                elif j == 9:
                    dp[i][j][k] = dp[i - 1][j - 1][k] \
                                  + dp[i - 1][j - 1][k - (1 << j)]
                else:
                    dp[i][j][k] = dp[i - 1][j + 1][k] \
                                  + dp[i - 1][j + 1][k - (1 << j)] \
                                  + dp[i - 1][j - 1][k] \
                                  + dp[i - 1][j - 1][k - (1 << j)]

    res = 0
    for i in range(1, n + 1):
        for j in range(10):
            # for k in range(1 << 10):
            #     if dp[i][j][k] != 0:
            #         print(i, j, summary(k), dp[i][j][k])
                # print(i, j, dp[i][j][(1 << 10) - 1])
            res += dp[i][j][(1 << 10) - 1]
    print(res)


if __name__ == '__main__':
    main()
