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
from utils import is_square, gcd
from tqdm import tqdm
import math


def main():
    i = 1
    solve = False
    while not solve:
        a = i * i
        for j in range(2, i):
            if solve:
                return
            c = j * j
            if not is_square(a - c):
                continue
            for k in range(1, j):
                if solve:
                    return
                d = k * k

                f = a - c
                b = d - f
                e = c - b
                print(a, b, c, d, e, f)
                if b < 0 or e < 0:
                    continue
                if not is_square(f):
                    continue
                if not is_square(b):
                    continue
                if not is_square(e):
                    continue

                if (c + d) % 2 == 1:
                    continue

                if (e + f) % 2 == 1:
                    continue

                if (c - d) % 2 == 1:
                    continue

                x = (a + b) // 2
                y = (e + f) // 2
                z = (c - d) // 2

                print(x, y, z, x + y + z)
                solve = True

        i += 1


if __name__ == '__main__':
    main()
