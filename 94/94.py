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
from tqdm import tqdm


if __name__ == '__main__':
    maxn = 1000000000
    res = 0
    has = set()
    for i in tqdm(range(1, int(math.sqrt(maxn / 3)) + 1)):
        for j in range(1, i):
            if gcd(i, j) == 1 and (i + j) % 2 == 1:
                a = i * i - j * j
                b = 2 * i * j
                c = i * i + j * j
                key = str(2 * c) + "#" + str(2 * a)
                if abs(c - 2 * a) == 1 and key not in has:
                    l = 2 * c + 2 * a
                    res += l
                    has.add(key)
                key = str(2 * c) + "#" + str(2 * b)
                if abs(c - 2 * b) == 1 and key not in has:
                    l = 2 * c + 2 * b
                    res += l
                    has.add(key)
    print(res)
