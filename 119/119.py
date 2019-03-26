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


def dig_sum(num):
    return sum([int(x) for x in str(num)])


if __name__ == '__main__':
    num = 1
    res = []
    while num < 100:
        for i in range(1, 21):
            if dig_sum(num ** i) == num:
                res.append(num ** i)
        num += 1
    print(sorted([x for x in res if x > 10])[29:])

