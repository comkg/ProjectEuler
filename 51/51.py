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


primes = get_all_prime(1000000)
primes_set = set(primes)


def get_max_cnt_primes_given_position(n, p):
    res = []
    n = list(n)
    for i in range(10):
        for j in p:
            n[j] = str(i)
        if int(''.join(n)) in primes_set:
            res.append(int(''.join(n)))
    return res


def get_max_cnt_primes(x):
    x = str(x)
    for i in range(1, 1 << len(x)):
        selected = []
        for j in range(len(x)):
            if i & (1 << j):
                selected.append(j)
        select_num = x[selected[0]]
        can = True
        for j in range(1, len(selected)):
            if select_num != x[selected[j]]:
                can = False
                break
        if can:
            prime_generate = get_max_cnt_primes_given_position(x, selected)
            if len(prime_generate) == 8 and min(prime_generate) == int(x):
                return True
    return False


if __name__ == '__main__':
    # print(primes.index(56003))
    # print(get_max_cnt_primes(111109))
    for prime in primes:
        if get_max_cnt_primes(prime):
            print(prime)


