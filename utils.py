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


def get_divisor_sum(x):
    """
    get the divisor sum.
    :param x: x
    :return: sum
    """
    if x <= 1:
        return 0
    res = 1
    for i in range(2, int(math.sqrt(x + 1)) + 1):
        if x % i == 0:
            if i * i == x:
                res += i
            else:
                res += (i + x // i)
    return res


def is_prime(x):
    """
    judge is prime.
    :param x: x
    :return: bool
    """
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x + 1)) + 1):
        if x % i == 0:
            return False
    return True


def gcd(a, b):
    """
    gcd
    :param a: a
    :param b: b
    :return: gcd
    """
    return a if b == 0 else gcd(b, a % b)


def get_all_prime(n):
    """
    get all primes less than n
    :param n: n
    :return: list of prime
    """
    res = []
    prime = [True for _ in range(n)]
    for i in range(2, n):
        if prime[i]:
            res.append(i)
            for j in range(i + i, n, i):
                prime[j] = False
    return res


def get_prime_factors(x):
    """
    get prime factors.
    :param x: x
    :return: prime factors list
    """
    primes = get_all_prime(x)
    res = []
    for prime in primes:
        while x % prime == 0:
            res.append(prime)
            x //= prime
    return res


def quick_pow_mod(x, y, mod):
    res = 1
    while y > 0:
        if y & 1:
            res = (res * x) % mod
        x = (x * x) % mod
        y = y >> 1
    return res
