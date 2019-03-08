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
import math
from tqdm import tqdm
import sys
sys.setrecursionlimit(100000)

n = 1000001

res = {}


def calc(x):
    ans = 0
    for i in range(2, int(math.sqrt(x + 0.1))):
        if x % i != 0:
            continue
        if i * i == x:
            ans += i
        else:
            ans += (i + x // i)
    return ans + 1


def find(x, cnt, origin, has):
    # print(x, cnt, origin)
    if cnt != 0 and x == origin:
        res[x] = has
        return
    if x in res:
        return
    if cnt != 0 and x in has[:-1]:
        return
    tem = calc(x)
    if tem < n:
        has.append(tem)
        find(tem, cnt + 1, origin, has)


if __name__ == '__main__':
    # ind(804, 0, 804, [804])
    # print(res[180])
    for i in tqdm(range(1, n)):
        find(i, 0, i, [i])
    # ans = 0
    # for i in range(1, n):
    #     if res[i] >= ans:
    #         ans = res[i]
    #         print(i)
    ans = 0
    for key in res:
        if len(res[key]) > ans:
            ans = len(res[key])
            print(res[key], min(res[key]))
