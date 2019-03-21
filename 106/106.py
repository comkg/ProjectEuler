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


def need_to_judge(x, y, n):
    res_x = []
    res_y = []
    for i in range(n):
        if (x >> i) & 1:
            res_x.append(i)
        if (y >> i) & 1:
            res_y.append(i)
    # print(any([x < y for x, y in zip(res_x, res_y)]))
    return len(res_x) == len(res_y) and not all([x < y for x, y in zip(res_x, res_y)])


if __name__ == '__main__':
    n = 12
    res = 0
    for i in range(1, (1 << n)):
        for j in range(i + 1, (1 << n)):
            if i & j == 0 and need_to_judge(i, j, n):
                res += 1
    print(res)

