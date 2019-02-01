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


if __name__ == '__main__':
    res = {}
    cnt = 0
    for i in range(2, int(math.sqrt(1500001 / 2))):
        for j in range(1, i):
            if (i + j) & 1 and gcd(i, j) == 1:
                a = i * i - j * j
                b = 2 * i * j
                c = i * i + j * j
                # print(a, b, c)
                L = a + b + c
                k = 1
                while k * L <= 1500000:
                    res[k * L] = res.get(k * L, 0) + 1
                    if res[k * L] == 1:
                        cnt += 1
                    elif res[k * L] == 2:
                        cnt -= 1
                    k += 1
    print(cnt)
