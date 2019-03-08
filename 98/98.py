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
from utils import is_square
import math


def is_anagram(x, y):
    return sorted(x) == sorted(y)


if __name__ == '__main__':
    with codecs.open('p098_words.txt', 'r', encoding='utf-8') as fin:
        words = [x[1:-1] for x in fin.read().split(",")]
        res = []
        for i in range(len(words)):
            for j in range(i):
                if is_anagram(words[i], words[j]):
                    res.append((words[i], words[j]))
        result = -1
        for i in range(10, 100000):
            tem = str(i * i)
            for item in res:
                if len(item[0]) == len(tem):
                    i_map = {}
                    can = True
                    for x in range(len(tem)):
                        if item[0][x] in i_map and i_map[item[0][x]] != tem[x]:
                            can = False
                            break
                        if item[0][x] not in i_map and tem[x] in i_map.values():
                            can = False
                            break
                        i_map[item[0][x]] = tem[x]
                    if not can:
                        continue
                    target = [i_map[x] for x in item[1]]
                    if target[0] == '0':
                        continue
                    ans = int(''.join(target))
                    if is_square(ans):
                        print(item, i * i, ans, i, int(math.sqrt(ans + 0.1)))
                        result = max(result, max(i, int(math.sqrt(ans + 0.1))))
        print(result)

