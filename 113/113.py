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
    n = 102
    dp = []
    for l in range(n):
        tem_l = []
        for i in range(10):
            tem_i = []
            for j in range(10):
                tem_i.append(0)
            tem_l.append(tem_i)
        dp.append(tem_l)
    for i in range(10):
        dp[1][i][i] = 1
    for i in range(10):
        for j in range(i + 1):
            dp[2][i][j] = 1
    for l in range(3, n):
        for i in range(10):
            for j in range(i + 1):
                for k in range(i + 1):
                    dp[l][i][j] += dp[l - 1][k][j]

    res = 0
    for l in range(1, 101):
        for i in range(1, 10):
            for j in range(i + 1):
                res += dp[l][i][j]
        for i in range(1, 10):
            for j in range(i + 1, 10):
                res += dp[l][j][i]
    print(res)
