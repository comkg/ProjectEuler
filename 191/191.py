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
    n = 30
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        dp[i][0][0] = dp[i - 1][0][0] + dp[i - 1][1][0] + dp[i - 1][2][0]
        dp[i][0][1] = dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][1][0] \
            + dp[i - 1][1][1] + dp[i - 1][2][0] + dp[i - 1][2][1]
        dp[i][1][0] = dp[i - 1][0][0]
        dp[i][1][1] = dp[i - 1][0][1]
        dp[i][2][0] = dp[i - 1][1][0]
        dp[i][2][1] = dp[i - 1][1][1]
        print(i, f"00:{dp[i][0][0]} 01:{dp[i][0][1]} 10:{dp[i][1][0]} 11:{dp[i][1][1]} 20:{dp[i][2][0]} 21:{dp[i][2][1]}")
    res = 0
    for i in range(3):
        res += dp[n][i][0] + dp[n][i][1]
    print(res)


if __name__ == '__main__':
    main()
