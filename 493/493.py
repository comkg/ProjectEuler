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
    n = 20
    dp = [[0 for _ in range(8)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        remain = 70 - i + 1
        for j in range(1, i + 1):
            if j > 7:
                continue
            dp[i][j] = dp[i - 1][j] * ((10 * j - i + 1) / remain) \
                + dp[i - 1][j - 1] * ((10 * (8 - j)) / remain)
    print(dp[20])
    res = 0
    for i in range(1, 8):
        res += dp[n][i] * i
    print(res)


if __name__ == '__main__':
    main()
