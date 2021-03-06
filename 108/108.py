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

limit = 2 * 4000000 - 1
res = None
primes = get_all_prime(47)


def find(cur, pid, num, up):
    if num >= limit:
        global res
        if res is None or cur < res:
            res = cur
        return
    if pid == len(primes):
        return
    for i in range(1, up + 1):
        find(cur * (primes[pid] ** i), pid + 1, num * (2 * i + 1), i)


if __name__ == '__main__':
    find(1, 0, 1, 30)
    print(res)
    # print(len(primes), primes)

