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
    n = 100
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    cnt = 0
    for i in range(1, n):
        # print()
        # print(i, end="--->")
        tem = 0
        for j in range(i + 1):
            if j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
            if dp[i][j] % 7 != 0:
                cnt += 1
                tem += 1
                # print(j, end=" ")
        # if i % 7 != 0:
        print(i, tem)
    print()
    print(cnt)


if __name__ == '__main__':
    main()
