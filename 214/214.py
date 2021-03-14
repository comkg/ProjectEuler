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
from utils import get_all_prime, euler_func

cache = {}


def path_length(x, dep):
    if x in cache:
        return cache[x]
    if x == 1:
        return 1
    res = path_length(euler_func(x), dep + 1) + 1
    cache[x] = res
    return res


def main():
    n = 40000000
    m = 25
    all_primes = get_all_prime(n)
    res = 0
    for prime in tqdm(all_primes):
        if path_length(prime, 0) == m:
            print(prime)
            res += prime
    print(res)


if __name__ == '__main__':
    main()
