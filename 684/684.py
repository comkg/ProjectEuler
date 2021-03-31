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
from utils import quick_pow_mod


mod = 1000000007


def find_inv(n):
    return quick_pow_mod(n, mod - 2, mod)


def calc(n):
    cur = n % 9
    mul = n // 9
    res = 0
    if mul > 0:
        n = mul - 1
        a = 10
        x = 45
        b = 81
        res = quick_pow_mod(10, n + 1, mod)
        res = (res - 1) % mod
        res = (res * find_inv(a - 1)) % mod
        res = (res * x) % mod

        t_res = quick_pow_mod(a, n + 1, mod)
        t_res = (t_res - a) % mod
        t_res = (t_res * find_inv(a - 1)) % mod
        t_res = (t_res - n) % mod
        t_res = (t_res * find_inv(a - 1)) % mod
        t_res = (t_res * b) % mod

        res = (res + t_res) % mod
    if cur > 0:
        n = mul
        a = 10
        x = (1 + cur) * cur // 2
        b = cur * 9
        t_res = quick_pow_mod(a, n, mod)
        t_res = (t_res * x) % mod

        p_res = quick_pow_mod(a, n, mod)
        p_res = (p_res - 1) % mod
        p_res = (p_res * find_inv(a - 1)) % mod
        p_res = (p_res * b) % mod

        t_res = (t_res + p_res) % mod

        res = (res + t_res) % mod
    return res


def main():
    # print(calc(1))
    pre = 0
    cur = 1
    cnt = 0
    res = 0
    while cnt < 89:
        t = pre
        pre = cur
        cur = cur + t
        cnt += 1
        print(cur, cnt)
        res = (res + calc(cur)) % mod
    print(res)


if __name__ == '__main__':
    main()
    # print(isprime(1000000007))
