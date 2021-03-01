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

res = {
    1: {1: 11, 3: 7, 7: 3, 9: 9},
    3: {1: 3, 3: 11, 7: 9, 9: 7},
    5: {7: 5},
    7: {1: 7, 3: 9, 7: 11, 9: 3},
    9: {1: 9, 3: 3, 7: 7, 9: 11}
}


def find_d(x, y):
    x = x % 10
    y = y % 10
    return res[x][y]


def find_target(x, y):
    d = find_d(x, y)
    str_x = str(x)
    while True:
        tem = str(d * y)
        if tem[-len(str_x):] == str_x:
            return d * y
        d += 10


if __name__ == '__main__':
    # 18612760000617135
    n = 1000010
    primes = get_all_prime(n)
    print(primes[-8:])
    # result = 0
    # for i in range(2, len(primes) - 1):
    #     print(primes[i], primes[i + 1])
    #     tem = find_target(primes[i], primes[i + 1])
    #     print(tem)
    #     result += tem
    # print(result)
    print(find_target(999983, 1000003) + 18612760000617135)
