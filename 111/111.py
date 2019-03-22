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
from itertools import combinations
from utils import is_prime


ans = []


def fill(items, pos, filled, target, tl):
    if pos == tl:
        if filled[0] != 0:
            res = 0
            for dig in filled:
                res = res * 10 + dig
            if is_prime(res):
                global ans
                ans.append(res)
        return
    if pos in items:
        filled.append(target)
        fill(items, pos + 1, filled, target, tl)
        filled.pop()
    else:
        for i in range(10):
            filled.append(i)
            fill(items, pos + 1, filled, target, tl)
            filled.pop()


if __name__ == '__main__':
    n = 10
    res = 0
    for i in range(10):
        ans.clear()
        for l in range(n - 1, 0, -1):
            for item in combinations(range(n), l):
                fill(list(item), 0, [], i, n)
            if len(ans) > 0:
                print(i, l, ans, sum(ans))
                res += sum(ans)
                break
    print(res)
