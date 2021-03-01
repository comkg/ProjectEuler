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


def is_all_odd(x):
    while x > 0:
        if x & 1 != 1:
            return False
        x = x // 10
    return True


def reverse(x):
    res = 0
    while x > 0:
        res = res * 10 + (x % 10)
        x = x // 10
    return res


if __name__ == '__main__':
    n = 1000000000
    res = 0
    for i in range(1, n):
        if i % 1000000 == 0:
            print(i)
        if i % 10 == 0:
            continue
        # print(i + reverse(i))
        if is_all_odd(i + reverse(i)):
            # print(i, i + reverse(i))
            res += 1
    print(res)
