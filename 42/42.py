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
import codecs


def is_triangle_number(x):
    l, r = 1, x
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if mid * (mid + 1) // 2 < x:
            l = mid + 1
        else:
            res = mid
            r = mid - 1
    return res * (res + 1) // 2 == x


if __name__ == '__main__':
    with codecs.open('words.txt', 'r', encoding='utf-8') as fin:
        res = 0
        for word in fin.read().strip().split(","):
            word = word.replace("\"", "")
            if is_triangle_number(sum([ord(x) - ord('A') + 1 for x in word])):
                res += 1
        print(res)
