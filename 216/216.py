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
from sympy import isprime

from utils import miller_rabin, get_all_prime


prime_max = 1000000


def is_prime(n, primes):
    if n <= prime_max:
        return n in primes
    return miller_rabin(n)


def main():
    primes = set(get_all_prime(prime_max))
    n = 50000000
    res = 0
    for i in tqdm(range(1, n + 1)):
        if isprime(2 * i * i - 1):
            res += 1
    print(res)


if __name__ == '__main__':
    main()
    # 5437851
    # 5437853
