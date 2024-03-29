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
import itertools
import random
from tqdm import tqdm


fibonacci_cache = {}


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
    for i in tqdm(range(2, n)):
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


def is_square(x):
    if x < 1:
        return False
    tem = int(math.sqrt(x))
    return tem * tem == x


def get_continued_fractions(x):
    """
    continued fractions.
    :param x: x
    :return: if x is square return, else continued fractions
    """
    if is_square(x):
        return
    int_part = int(math.sqrt(x))
    up_part = 1
    bias_part = -int_part
    while True:
        int_part = int(up_part * (math.sqrt(x) - bias_part) / (x - bias_part * bias_part))
        up_part_tem = x - bias_part * bias_part
        up_part = up_part_tem // gcd(up_part_tem, up_part)
        bias_part = -bias_part - int_part * up_part
        yield int_part


def permutations(pool):
    return itertools.permutations(pool)


def euler_func(x):
    res = x
    i = 2
    while i * i <= x:
        if x % i == 0:
            x //= i
            res = res - res // i
        while x % i == 0:
            x //= i
        i += 1
    if x > 1:
        res = res - res // x
    return res


def miller_rabin(n):
    if n == 1:
        return False
    d = n - 1
    i = random.randint(1, n-1)
    while d != 1:
        if quick_pow_mod(i, d, n) == 1:
            if d % 2 != 0:
                return True
            d = d // 2
            if quick_pow_mod(i, d, n) == n - 1:
                return True
        else:
            return False
    return True


def fibonacci(n, mod):
    if n == 0:
        return 0
    if n == 1:
        return 1
    global fibonacci_cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    f_n = fibonacci((n + 1) // 2, mod)
    f_n_1 = fibonacci((n + 1) // 2 - 1, mod)
    if n & 1:
        res = ((f_n * f_n) + (f_n_1 * f_n_1)) % mod
    else:
        res = f_n * (2 * f_n_1 + f_n) % mod
    fibonacci_cache[n] = res
    return res
