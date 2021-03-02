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

from utils import get_all_prime


def find_all_nums():
    n = 51
    res = [[0 for _ in range(n)] for _ in range(n)]
    res[0][0] = 1
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    result = []
    for i in range(n):
        for j in range(n):
            if res[i][j] != 0:
                result.append(res[i][j])
    return set(result)


def is_square_free(x, primes):
    for prime in primes:
        if prime * prime > x:
            break
        if x % (prime * prime) == 0:
            return False
    return True


if __name__ == '__main__':
    result = find_all_nums()
    print(result)
    max_num = max(result)
    all_primes = get_all_prime(int(math.sqrt(max_num) + 1))
    res = 0
    for item in result:
        if is_square_free(item, all_primes):
            res += item
    print(res)
