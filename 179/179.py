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
from utils import get_all_prime


def get_factor_cnt(x, all_primes):
    res = 1
    for prime in all_primes:
        if x % prime == 0:
            tem = 1
            while x % prime == 0:
                tem += 1
                x /= prime
            res *= tem
        if x == 1:
            break
    return res


if __name__ == '__main__':
    n = 10 ** 7
    res = [1 for _ in range(n + 1)]
    for i in tqdm(range(2, n + 1)):
        if res[i] == 1:
            for j in range(i, n, i):
                tem = 1
                tem_j = j
                while tem_j % i == 0:
                    tem += 1
                    tem_j /= i
                res[j] = res[j] * tem
    result = 0
    for i in range(2, n):
        if res[i] == res[i + 1]:
            result += 1
    print(result)
