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


def get_all_rotation(x):
    res = []
    x = str(x)
    for i in range(len(x)):
        res.append(int(x[i:len(x)] + x[:i]))
    return res


if __name__ == '__main__':
    # print(get_all_rotation(1234))
    primes = set(get_all_prime(1000000))
    res = 0
    for prime in primes:
        print(prime)
        print(get_all_rotation(prime))
        if all([x in primes for x in get_all_rotation(prime)]):
            res += 1
    print(res)
