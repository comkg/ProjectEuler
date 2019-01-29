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


def get_ord_sum(x):
    return sum([ord(c) for c in x])


if __name__ == '__main__':
    with codecs.open('p059_cipher.txt', 'r', encoding='utf-8') as fin:
        line = [int(x) for idx, x in enumerate(fin.read().strip().split(','))]
        num_cnt = {x: line.count(x) for x in line}
        print(sorted(num_cnt.items(), key=lambda x: x[1]))
        key = 'god'
        res = ''
        for idx, x in enumerate(line):
            res += chr(ord(key[idx % 3]) ^ x)
        print(res)
        print(get_ord_sum(res))
