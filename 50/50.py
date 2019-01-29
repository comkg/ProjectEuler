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
from utils import get_all_prime, is_prime


if __name__ == '__main__':
    n = 1000000
    primes = get_all_prime(n)
    primes_set = set(primes)
    res = 0
    for i in range(len(primes)):
        # print(i)
        for j in range(i + 1, len(primes)):
            tem = sum(primes[i:j])
            if tem >= n:
                break
            if tem in primes_set and j - i > res:
                print(tem, j - i, primes[i:j])
                res = j - i
    print(res)
