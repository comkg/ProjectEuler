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


def judge(x):
    res = 0
    ox = x
    while x > 0:
        res += math.factorial(x % 10)
        x //= 10
    return res == ox


if __name__ == '__main__':
    res = 0
    print(judge(145))
    for i in range(3, 10000000):
        if judge(i):
            print(i)
            res += i
    print(res)
