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


def same(x, y):
    x = sorted(str(x))
    y = sorted(str(y))
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True


def is_valid(x):
    return same(x, 2 * x) and same(x, 3 * x) and same(x, 4 * x) and same(x, 5 * x) and same(x, 6 * x)


if __name__ == '__main__':
    i = 1
    while True:
        if is_valid(i):
            print(i)
            break
        i = i + 1

