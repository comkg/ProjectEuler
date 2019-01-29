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


def judge_palindrome(x):
    return str(x) == str(x)[::-1]


def is_lychrel_number(x):
    cnt = 1
    while cnt < 50:
        x = x + int(str(x)[::-1])
        if judge_palindrome(x):
            return False
        cnt += 1
    return True


if __name__ == '__main__':
    res = 0
    for i in range(10000):
        if is_lychrel_number(i):
            print(i)
            res += 1
    print(res)
