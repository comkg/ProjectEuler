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


def find_satisfy_cnt(idx, primes, total):
    l, r = idx, len(primes)
    res = -1
    while l <= r:
        mid = (l + r) // 2
        # print(l, r, mid)
        if primes[mid] * primes[idx] >= total:
            r = mid - 1
        else:
            l = mid + 1
            res = mid
    return res


if __name__ == '__main__':
    n = 10 ** 8
    all_primes = get_all_prime(n)
    res = 0
    for i in range(len(all_primes)):
        cnt = find_satisfy_cnt(i, all_primes, n)
        # print(all_primes[i], cnt, all_primes[cnt])
        if cnt != -1:
            res += (cnt - i + 1)
    print(res)
