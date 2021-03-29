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
import math
from sympy import isprime

from utils import gcd, get_all_prime


def main():
    n = 1504170715041707
    mod = 4503599627370517
    res = 0
    cur = 1
    pre_min = mod
    pre_i = 0
    print(gcd(n, mod))
    print(isprime(n))
    print(isprime(mod))
    # primes = get_all_prime(int(math.sqrt(n)) + 1)
    # for prime in primes:
    #     if n % prime == 0:
    #         cnt = 0
    #         while n % prime == 0:
    #             n //= prime
    #             cnt += 1
    #         print(prime, cnt)
    while True:
        tem = (n * cur) % mod
        # print(cur, tem)
        if tem < pre_min:
            print(cur, tem, cur - pre_i)
            res += tem
            pre_min = tem
            pre_i = cur
        if tem == 1:
            break
        if 10827725431 > cur >= 42298633:
            cur += 283827021
        elif cur >= 10827725431:
            cur += 11111552452
        else:
            cur += 1
    print(res)


if __name__ == '__main__':
    main()
    # 1 1504170715041707 1
    # 3 8912517754604 2
    # 506 2044785486369 503
    # 2527 1311409677241 2021
    # 4548 578033868113 2021
    # 11117 422691927098 6569
    # 17686 267349986083 6569
    # 24255 112008045068 6569
    # 55079 68674149121 30824
    # 85903 25340253174 30824
    # 202630 7346610401 116727
    # 724617 4046188430 521987
    # 1246604 745766459 521987
    # 6755007 428410324 5508403
    # 12263410 111054189 5508403
    # 42298633 15806432 30035223
    # 326125654 15397267 283827021
    # 609952675 14988102 283827021
    # 893779696 14578937 283827021
    # 1177606717 14169772 283827021
    # 1461433738 13760607 283827021
    # 1745260759 13351442 283827021
    # 2029087780 12942277 283827021
    # 2312914801 12533112 283827021
    # 2596741822 12123947 283827021
    # 2880568843 11714782 283827021
    # 3164395864 11305617 283827021
    # 3448222885 10896452 283827021
    # 3732049906 10487287 283827021
    # 4015876927 10078122 283827021
    # 4299703948 9668957 283827021
    # 4583530969 9259792 283827021
    # 4867357990 8850627 283827021
    # 5151185011 8441462 283827021
    # 5435012032 8032297 283827021
    # 5718839053 7623132 283827021
    # 6002666074 7213967 283827021
    # 6286493095 6804802 283827021
    # 6570320116 6395637 283827021
    # 6854147137 5986472 283827021
    # 7137974158 5577307 283827021
    # 7421801179 5168142 283827021
    # 7705628200 4758977 283827021
    # 7989455221 4349812 283827021
    # 8273282242 3940647 283827021
    # 8557109263 3531482 283827021
    # 8840936284 3122317 283827021
    # 9124763305 2713152 283827021
    # 9408590326 2303987 283827021
    # 9692417347 1894822 283827021
    # 9976244368 1485657 283827021
    # 10260071389 1076492 283827021
    # 10543898410 667327 283827021
    # 10827725431 258162 283827021
    # 21939277883 107159 11111552452
