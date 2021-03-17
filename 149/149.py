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


def generator():
    res = [[0 for _ in range(2000)] for _ in range(2000)]
    for k in range(1, 2000 * 2000 + 1):
        i = (k - 1) // 2000
        j = (k - 1) % 2000
        if k <= 55:
            res[i][j] = (100003 - 200003 * k + 300007 * k * k * k) % 1000000\
                        - 500000
        else:
            k24_i = (k - 25) // 2000
            k24_j = (k - 25) % 2000
            k55_i = (k - 56) // 2000
            k55_j = (k - 56) % 2000
            res[i][j] = (res[k24_i][k24_j] + res[k55_i][k55_j] + 1000000) \
                % 1000000 - 500000
    return res


def lcs(x):
    res = 0
    tem = 0
    for i in x:
        tem += i
        res = max(res, tem)
        if tem < 0:
            tem = 0
    return res


def main():
    mat = generator()
    res = 0
    for i in range(2000):
        tem_h = []
        tem_v = []
        for j in range(2000):
            tem_h.append(mat[i][j])
            tem_v.append(mat[j][i])
        res = max(res, max(lcs(tem_h), lcs(tem_v)))
    for i in range(3999):
        if i < 2000:
            s_i, s_j = i, 0
        else:
            s_i, s_j = 1999, i - 1999
        tem = []
        while s_i >= 0 and s_j < 2000:
            tem.append(mat[s_i][s_j])
            s_i -= 1
            s_j += 1
        res = max(res, lcs(tem))

    for i in range(3999):
        if i < 2000:
            s_i, s_j = 1999 - i, 0
        else:
            s_i, s_j = 0, i - 1999
        tem = []
        while s_i < 1000 and s_j < 2000:
            tem.append(mat[s_i][s_j])
            s_i += 1
            s_j += 1
        res = max(res, lcs(tem))

    print(res)


if __name__ == '__main__':
    main()
