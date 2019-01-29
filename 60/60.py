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


primes_set = set(get_all_prime(100000000))


def is_combine_prime(x, y):
    return int(str(x) + str(y)) in primes_set and int(str(y) + str(x)) in primes_set


def is_valid(pool):
    for i in range(len(pool)):
        for j in range(i):
            if not is_combine_prime(pool[i], pool[j]):
                return False
    return True


def get_key(x, y):
    return str(x) + '#' + str(y)


if __name__ == '__main__':
    primes = get_all_prime(10000)
    res = set()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if is_combine_prime(primes[i], primes[j]):
                res.add(get_key(primes[i], primes[j]))
    for a in range(len(primes)):
        # print(a)
        for b in range(a + 1, len(primes)):
            if get_key(primes[a], primes[b]) not in res:
                continue
            for c in range(b + 1, len(primes)):
                if get_key(primes[a], primes[c]) not in res \
                        or get_key(primes[b], primes[c]) not in res:
                    continue
                for d in range(c + 1, len(primes)):
                    if get_key(primes[a], primes[d]) not in res \
                            or get_key(primes[b], primes[d]) not in res \
                            or get_key(primes[c], primes[d]) not in res:
                        continue
                    for e in range(d + 1, len(primes)):
                        if get_key(primes[a], primes[e]) not in res \
                                or get_key(primes[b], primes[e]) not in res \
                                or get_key(primes[c], primes[e]) not in res \
                                or get_key(primes[d], primes[e]) not in res:
                            continue
                        if is_valid([primes[a], primes[b], primes[c], primes[d], primes[e]]):
                            print(primes[a], primes[b], primes[c], primes[d], primes[e])
                            print(sum([primes[a], primes[b], primes[c], primes[d], primes[e]]))

