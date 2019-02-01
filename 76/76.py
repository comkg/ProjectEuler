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
    for i in range(0, 105):
        tem = []
        for j in range(i + 1):
            if j == i:
                tem.append(1)
            else:
                tem.append(0)
        dp.append(tem)
    for i in range(1, 101):
        for j in range(1, i):
            d = i - j
            for k in range(1, min(j, d) + 1):
                # print(i, j, k, dp[d][k])
                dp[i][j] += dp[d][k]
                # print(dp[i][j])
    print(sum(dp[100]) - 1)
