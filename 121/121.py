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


if __name__ == '__main__':
    dp = []
    for i in range(16):
        dp.append([0] * 16)
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, 16):
        for j in range(i + 1):
            if j == i:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j] * i + dp[i - 1][j - 1]
    res = 0
    for i in range(8, 16):
        res += dp[15][i]
    cnt = 1
    for i in range(2, 17):
        cnt *= i
    print(cnt // res)
