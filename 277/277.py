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


cache = {}


def generate(n):
    if n % 3 == 0:
        return n // 3, "D"
    if n % 3 == 1:
        return (4 * n + 2) // 3, "U"
    return (2 * n - 1) // 3, "d"


def solve(n):
    res = ""
    ori_n = n
    while n > 1:
        if n in cache:
            res += cache[n]
            cache[ori_n] = res
            return res
        n, f = generate(n)
        res += f
    return res


def main():
    limit = 10 ** 15
    target = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
    # target = "UDD"
    cur = 4
    for i in range(1, len(target), 1):
        for j in range(3):
            tem = cur + j * (3 ** i)
            tem_str = solve(tem)
            if len(tem_str) > i and tem_str[i] == target[i]:
                cur = tem
    while cur <= limit:
        cur += (3 ** len(target))
    print(cur)


if __name__ == '__main__':
    main()
