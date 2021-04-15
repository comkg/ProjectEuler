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


def calc(n):
    res = 1
    cur = 2
    while cur != 1:
        cur = (2 * cur) % (n - 1)
        res += 1
    return res


def get_all_factors(n):
    res = set()
    for i in tqdm(range(1, int(math.sqrt(n) + 1))):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return res


def satisfy(factor, n):
    for i in range(2, n):
        if (2 ** i - 1) % factor == 0:
            return False
    return True


def main():
    # for i in range(4, 2000, 2):
    #     print(i, calc(i))
    k = 60
    n = 2 ** k - 1
    factors = get_all_factors(n)
    res = 0
    for factor in factors:
        if satisfy(factor, k):
            res += (factor + 1)
    print(res)


if __name__ == '__main__':
    main()
