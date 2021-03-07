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
import math

from utils import get_all_prime


if __name__ == '__main__':
    n = 100000002
    all_primes = set(get_all_prime(n))
    res = 0
    for prime in tqdm(all_primes):
        n = prime - 1
        flag = True
        for i in range(2, int(math.sqrt(prime)) + 1):
            if n % i == 0:
                if i + n // i not in all_primes:
                    flag = False
                    break
        if flag:
            res += n
    print(res)
