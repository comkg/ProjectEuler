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

from utils import is_square


def fac_square_sum(n):
    res = 0
    for i in range(1, int(math.sqrt(n + 1))):
        if n % i == 0:
            res += i * i
            if i * i != n:
                res += (n // i) * (n // i)
    return res


def main():
    n = 1000000
    for i in range(1, n):
        if is_square(fac_square_sum(i)):
            print(i)


if __name__ == '__main__':
    # print(fac_square_sum(10))
    main()
