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


def calc_fifth_sum(x):
    res = 0
    while x > 0:
        res += math.pow(x % 10, 5)
        x //= 10
    return res


if __name__ == '__main__':
    res = 0
    for i in range(2, 1000000):
        if i == calc_fifth_sum(i):
            print(i)
            res += i
    print(res)
