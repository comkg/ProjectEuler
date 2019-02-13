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
from utils import get_all_prime
import math


if __name__ == '__main__':
    target = 50000000
    res = set()
    n = int(math.sqrt(target))
    primes = get_all_prime(n)
    p_l = len(primes)
    for i in range(p_l):
        for j in range(p_l):
            if primes[i] ** 2 + primes[j] ** 3 > target:
                break
            for k in range(p_l):
                tem = primes[i] ** 2 + primes[j] ** 3 + primes[k] ** 4
                if tem >= target:
                    break
                res.add(tem)
    print(len(res))
