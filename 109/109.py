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
from itertools import combinations_with_replacement


def score(items):
    res = 0
    for item in items:
        res += item[0] * item[1]
    return res


if __name__ == '__main__':
    items = []
    for i in range(1, 21):
        items.extend([(i, 1), (i, 2), (i, 3)])
    items.append((25, 1))
    items.append((25, 2))
    res = 0
    for i in range(1, 4):
        for item in combinations_with_replacement(items, i):
            doubles = set([x for x in list(item) if x[1] == 2])
            if score(item) < 100:
                res += len(doubles)
    print(res)
