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


def is_square(x):
    tem = int(math.sqrt(x))
    return tem * tem == x


def make_str(a, b, c):
    return str(a) + '#' + str(b) + '#' + str(c)


def get_period(x):
    if is_square(x):
        return []
    int_part = int(math.sqrt(x))
    up_part = 1
    bias_part = -int_part
    res = [make_str(int_part, up_part, bias_part)]
    while True:
        int_part = int(up_part * (math.sqrt(x) - bias_part) / (x - bias_part * bias_part))
        up_part_tem = x - bias_part * bias_part
        up_part = up_part_tem // gcd(up_part_tem, up_part)
        bias_part = -bias_part - int_part * up_part
        key = make_str(int_part, up_part, bias_part)
        if key in res:
            return res[res.index(key):]
        res.append(key)


if __name__ == '__main__':
    res = 0
    for i in range(2, 10001):
        if len(get_period(i)) & 1:
            res += 1
    print(res)
