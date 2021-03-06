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
from utils import get_all_prime


if __name__ == '__main__':
    primes = set(get_all_prime(1000000000))
    pre_cnt = 8
    for i in range(9, 100000, 2):
        tem_cnt = 0
        for j in range(4):
            if i * i - j * (i - 1) in primes:
                tem_cnt += 1
        if (pre_cnt + tem_cnt) / (2 * i - 1) < 0.1:
            print(i)
            break
        pre_cnt += tem_cnt
        print(i, pre_cnt)
