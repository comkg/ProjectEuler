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


def is_satisfy(x, primes):
    res = []
    for prime in primes:
        if prime > x:
            break
        if x % prime == 0:
            res.append(prime)
            if len(res) > 2:
                return []
            while x % prime == 0:
                x //= prime
    return res


if __name__ == '__main__':
    n = 10000001
    res = [[] for _ in range(n)]
    for i in range(2, n):
        if len(res[i]) == 0:
            for j in range(i + i, n, i):
                res[j].append(i)
    r = 0
    i_r = set()
    for i in range(n - 1, 2, -1):
        if len(res[i]) == 2:
            key = str(res[i][0]) + "-" + str(res[i][1])
            if key in i_r:
                continue
            r += i
            i_r.add(key)
    print(r)
