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
    dp = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n + 1)]
    for i in range(1, 10):
        dp[1][0][i] = 1
    for i in range(2, n + 1):
        for j in range(10):
            for k in range(10):
                for _j_p in range(10):
                    if _j_p + j + k <= 9:
                        dp[i][j][k] += dp[i - 1][_j_p][j]
    res = 0
    for i in range(10):
        for j in range(10):
            res += dp[n][i][j]
    print(res)


if __name__ == '__main__':
    main()
