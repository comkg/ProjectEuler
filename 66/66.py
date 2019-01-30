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
from utils import is_square, get_continued_fractions
import math


if __name__ == '__main__':
    res = 0
    for d in range(2, 1001):
        if is_square(d):
            continue
        h_1, h_2 = int(math.sqrt(d)), 1
        k_1, k_2 = 1, 0
        ans = -1
        for item in get_continued_fractions(d):
            h_t = item * h_1 + h_2
            k_t = item * k_1 + k_2
            if h_t * h_t - d * k_t * k_t == 1:
                ans = h_t
                break
            h_2 = h_1
            h_1 = h_t
            k_2 = k_1
            k_1 = k_t
        if ans > res:
            print(d, ans)
            res = ans
