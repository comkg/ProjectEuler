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

from utils import get_all_prime

n = 2 ** 50
res = n


def find(dep, cur_idx, square_sum, primes):
    num = n // square_sum
    global res
    if dep & 1:
        res -= num
    elif dep != 0:
        res += num
    for i in range(cur_idx, len(primes), 1):
        tem = square_sum * primes[i] * primes[i]
        if tem > n:
            return
        find(dep + 1, i + 1, tem, primes)


def main():
    primes = get_all_prime(int(math.sqrt(n)) + 1)
    find(0, 0, 1, primes)
    print(res)


if __name__ == '__main__':
    main()
    #
    # 1125899906842624
    # 1125899906842623
    # 616714581538888
    # 684465069551779
    # 684465069122123
    # 684465068462259
    # 684465068461129
    # 684465068461130
    # 684465068461128
    # 684465068460366
    # 684465068460365

