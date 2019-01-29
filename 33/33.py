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
from utils import gcd


def can_reduce(x, y):
    for i in range(1, 10):
        if str(i) in str(x) and str(i) in str(y):
            return i
    return -1


def reduce(x, y, z):
    return int(str(x).replace(z, "", 1)), int(str(y).replace(z, "", 1))


if __name__ == '__main__':
    frac_a = 1
    frac_b = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            dit = can_reduce(i, j)
            if dit > 0:
                x, y = reduce(i, j, str(dit))
                if x * j == y * i:
                    frac_a *= i
                    frac_b *= j
    print(frac_a, frac_b)
    print(frac_b // gcd(frac_b, frac_a))
