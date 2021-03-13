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


def main():
    n = 16
    dp = [[0 for _ in range(8)] for _ in range(n + 1)]
    dp[1][0] = 13
    dp[1][1] = 0
    dp[1][2] = 1
    dp[1][4] = 1
    for i in range(2, n + 1):
        for j in range(8):
            dp[i][j] = dp[i - 1][j] * 13
            if j & 1 != 0:
                dp[i][j] += dp[i - 1][j ^ 1] + dp[i - 1][j]
            if j & 2 != 0:
                dp[i][j] += dp[i - 1][j ^ 2] + dp[i - 1][j]
            if j & 4 != 0:
                dp[i][j] += dp[i - 1][j ^ 4] + dp[i - 1][j]
    res = 0
    for i in range(3, n + 1):
        res += dp[i][7]
    print(hex(res).upper())


if __name__ == '__main__':
    main()
