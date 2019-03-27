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


def is_palindromic(x):
    if x == 0:
        return False
    x = str(x)
    return x == x[::-1]


if __name__ == '__main__':
    n = 10000
    target = 100000000
    res = 0
    has = set()
    for i in range(1, n):
        tem = i * i + (i + 1) * (i + 1)
        num = i + 2
        while tem < target:
            if is_palindromic(tem):
                print(tem)
                if tem not in has:
                    res += tem
                    has.add(tem)
            tem += num * num
            num += 1
    print(res)
