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


def q_pow(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res *= x
        x *= x
        y //= 2
    return res


def u(x):
    res = 0
    for i in range(11):
        if i & 1:
            res -= q_pow(x, i)
        else:
            res += q_pow(x, i)
    return res


def solve(x, n):
    for i in range(n):
        for j in range(i + 1, n):
            tem = []
            for k in range(i, n + 1):
                tem.append(x[j][k] * x[i][i] - x[j][i] * x[i][k])
            x[j] = [0] * (n - len(tem) + 1) + tem
    res = []
    for i in range(n - 1, -1, -1):
        sum = 0
        # print(res, x[i])
        for j in range(len(res)):
            sum += res[j] * x[i][n - j - 1]
        res.append((x[i][-1] - sum) // x[i][i])
    return res


if __name__ == '__main__':
    # solve([[4, 3, 2, 9], [3, 5, 4, 12], [2, 4, 7, 13]], 3)
    # solve([[2, 1, 5], [1, 3, 5]], 2)
    # solve([[1, 1, 1, 1], [4, 2, 1, 8], [9, 3, 1, 27]], 3)
    ux = [u(i) for i in range(12)]
    print(ux)
    ans = 1
    for i in range(1, 11):
        x = []
        for j in range(1, i + 2):
            tem = []
            for k in range(i, -1, -1):
                tem.append(q_pow(j, k))
            # print(j)
            tem.append(ux[j])
            x.append(tem)
        res = solve(x, i + 1)
        print(res)
        tem = 0
        if i == 10:
            continue
        for j in range(len(res)):
            tem += res[j] * q_pow(i + 2, j)
        print(tem)
        ans += tem
    print(ans)
