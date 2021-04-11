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
from utils import quick_pow_mod, gcd


def g(n):
    res = 1
    for i in range(1, n):
        if gcd(i, n) == 1:
            print(n, i)
            res *= i
    return res


def main():
    n = 10
    mod = 1000000007
    res = 1

    for i in range(2, n, 1):
        cnt = (n - i) - (n - i) // i
        res = (res * quick_pow_mod(i, cnt, mod)) % mod

    print(res)
    res = 1
    for i in range(1, 11):
        # print(i, g(i))
        res *= g(i)
    print(res, res % mod)


if __name__ == '__main__':
    # may relate to problem 193
    main()
