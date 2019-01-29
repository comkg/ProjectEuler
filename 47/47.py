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


n = 1000000

primes = get_all_prime(n)


def get_prime_factors(x):
    """
    get prime factors.
    :param x: x
    :return: prime factors list
    """
    res = []
    for prime in primes:
        if prime > x:
            break
        while x % prime == 0:
            res.append(prime)
            x //= prime
    return res


if __name__ == '__main__':

    for i in range(1, n):
        # print(i)
        if len(set(get_prime_factors(i))) == 4 \
                and len(set(get_prime_factors(i + 1))) == 4 \
                and len(set(get_prime_factors(i + 2))) == 4 \
                and len(set(get_prime_factors(i + 3))) == 4:
            print(i)
