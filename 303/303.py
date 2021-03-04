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
from tqdm import tqdm


def is_satisfy(x):
    while x > 0:
        if x % 10 > 2:
            return False
        x //= 10
    return True


def find(x):
    queue = [1, 2]
    idx = 0
    while True:
        tem = queue[idx]
        if tem % x == 0:
            return tem // x
        queue.append(tem * 10)
        queue.append(tem * 10 + 1)
        queue.append(tem * 10 + 2)
        idx += 1


if __name__ == '__main__':
    res = 0
    for i in tqdm(range(1, 11)):
        i_r = find(i)
        print(i, i_r)
        res += i_r
    # 9999 res: 1111333355557778 ref 9,99,999
    res += 1111333355557778 + 1
    print(res)
