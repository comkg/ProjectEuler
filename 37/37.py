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


def get_all_sub_num(x):
    res = [x]
    x = str(x)
    for i in range(1, len(x)):
        res.append(int(x[:i]))
        res.append(int(x[len(x) - i:]))
    return set(res)


if __name__ == '__main__':
    primes = set(get_all_prime(1000000))
    primes_single = set(get_all_prime(10))
    res = 0
    for prime in primes:
        if all([x in primes and prime not in primes_single for x in get_all_sub_num(prime)]):
            res += prime
            print(prime, get_all_sub_num(prime))
    print(res)
