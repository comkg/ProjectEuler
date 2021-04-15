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


flag = False


def find(ns, dep, cur_idx, cur_sum, target):
    global flag
    if cur_idx == len(ns):
        if dep > 1 and cur_sum == target:
            flag = True
        return
    if flag:
        return
    tem = 0
    for j in range(cur_idx, len(ns)):
        tem = tem * 10 + int(ns[j])
    if cur_sum + tem < target:
        return
    for i in range(cur_idx + 1, len(ns) + 1):
        tem = 0
        for j in range(cur_idx, i):
            tem = tem * 10 + int(ns[j])
        find(ns, dep + 1, i, cur_sum + tem, target)


def main():
    global flag
    print(flag)
    find(str(6724), 0, 0, 0, 82)
    print(flag)
    n = 10 ** 12
    res = 0
    for i in tqdm(range(1, int(math.sqrt(n)) + 1)):
        flag = False
        find(str(i * i), 0, 0, 0, i)
        if flag:
            # print(i, i * i)
            res += i * i
    print(res)


if __name__ == '__main__':
    main()
