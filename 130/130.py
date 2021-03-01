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
from utils import is_prime


def solve(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    res = 1
    x = 1
    while x != 0:
        x = (x * 10 + 1) % n
        res += 1
    return res


if __name__ == '__main__':
    n = 3
    cnt = 0
    result = 0
    while cnt < 25:
        # print(n)
        n += 2
        if is_prime(n):
            continue
        res = solve(n)
        if res == 0:
            continue
        if (n - 1) % solve(n) == 0:
            print(n)
            result += n
            cnt += 1
    print(result)
