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
from utils import get_all_prime, quick_pow_mod


if __name__ == '__main__':
    n = 1000000000
    primes = get_all_prime(n // 1000)
    cnt = 0
    res = 0
    for prime in primes[1:]:
        if quick_pow_mod(10, n, 9 * prime) == 1:
            cnt += 1
            res += prime
        if cnt == 40:
            break
    print(res)


