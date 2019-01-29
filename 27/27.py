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
from utils import is_prime


def calc_max_consecutive_len(a, b):
    i = 0
    while True:
        if not is_prime(i * i + a * i + b):
            return i
        i = i + 1


if __name__ == '__main__':
    max_len = 0
    res = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            value = calc_max_consecutive_len(a, b)
            if max_len < value:
                max_len = value
                res = a * b

    print(res)
