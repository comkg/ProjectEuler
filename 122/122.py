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
from copy import deepcopy


def find(numbers, res):
    if len(numbers) > 11:
        return
    if numbers[-1] not in res or res[numbers[-1]] > len(numbers) - 1:
        res[numbers[-1]] = len(numbers) - 1
    tem = deepcopy(numbers)
    for item in tem:
        if item + tem[-1] > 200:
            continue
        numbers.append(tem[-1] + item)
        find(numbers, res)
        numbers.pop()


if __name__ == '__main__':
    res = {}
    find([1], res)
    ans = 0
    print(sorted(res.items(), key=lambda x: x[0]))
    for i in range(1, 201):
        if i not in res:
            print(i)
        else:
            ans += res[i]
    print(ans)
