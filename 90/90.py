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
import itertools


def judge(x, y, item, jtem):
    return (x in item and y in jtem) or (x in jtem and y in item)


def exp(item):
    if 6 in item and 9 in item:
        return
    if 6 in item:
        item.append(9)
    elif 9 in item:
        item.append(6)


def judge_all(item, jtem):
    return judge(0, 1, item, jtem) \
           and judge(0, 4, item, jtem) \
           and judge(0, 9, item, jtem) \
           and judge(1, 6, item, jtem) \
           and judge(2, 5, item, jtem) \
           and judge(3, 6, item, jtem) \
           and judge(4, 9, item, jtem) \
           and judge(6, 4, item, jtem) \
           and judge(8, 1, item, jtem)


if __name__ == '__main__':
    cnt = 0
    for item in itertools.combinations(list(range(10)), 6):
        for jtem in itertools.combinations(list(range(10)), 6):
            item = list(item)
            jtem = list(jtem)
            exp(item)
            exp(jtem)
            if judge_all(item, jtem):
                print(item, jtem)
                cnt += 1
    print(cnt // 2)
