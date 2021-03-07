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
from utils import gcd, get_all_prime, euler_func


def find(x):
    cnt = 0
    for i in range(1, x):
        if gcd(i, x) == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(euler_func(12))
    n = 40
    all_primes = get_all_prime(n)
    target = 15499 / 94744
    best = 1.
    print(target)
    tem_cal = 2
    for prime in all_primes[1:]:
        for i in range(1, prime):
            tem_num = euler_func(tem_cal * i) / (tem_cal * i - 1)
            print(tem_cal * i, tem_num)
            if tem_num < target:
                print(i)
                break
        tem_cal *= prime


    # 6, 30, 210, 2310
    # 2,3, 2,3,5, 2,3,5,7
