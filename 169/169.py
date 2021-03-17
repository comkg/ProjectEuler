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
    n = 10 ** 25
    digs = []
    while n > 0:
        digs.append(n % 2)
        n = n // 2
    dp = [[0, 0] for _ in range(len(digs) + 1)]
    dp[0][0] = 1
    cur = 0
    for i in range(1, len(digs) + 1):
        if digs[i - 1] == 1:
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = cur * (dp[i - 1][0] + dp[i - 1][1]) + dp[i - 1][1]
            cur = 0
            continue
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        cur += 1
        # print(dp[i])
    print(dp[len(digs)][0] + dp[len(digs)][1])
    # print(dp[len(digs)][1])


if __name__ == '__main__':
    main()
