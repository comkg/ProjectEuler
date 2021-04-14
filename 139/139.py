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

from utils import gcd


def main():
    n = 100000000
    res = 0
    for i in range(2, int(math.sqrt(n / 2)), 1):
        for j in range(1, i):
            if (i + j) & 1 and gcd(i, j) == 1:
                a = i * i - j * j
                b = 2 * i * j
                c = i * i + j * j
                l = a + b + c
                k = 1
                if c % (b - a) == 0:
                    while k * l < n:
                        res += 1
                        k += 1
    print(res)


if __name__ == '__main__':
    # relate to problem 75
    # may ref:
    # https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
    main()
