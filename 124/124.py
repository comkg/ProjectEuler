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


def fac(n, primes):
    res = 1
    idx = 0
    while n > 1:
        if n % primes[idx] == 0:
            res *= primes[idx]
            while n % primes[idx] == 0:
                n //= primes[idx]
        idx += 1
    return res


if __name__ == '__main__':
    primes = get_all_prime(100000)
    res = []
    for i in range(1, 100001):
        res.append((i, fac(i, primes)))
    res = sorted(res, key=lambda x: (x[1], x[0]))
    print(res[9999])
