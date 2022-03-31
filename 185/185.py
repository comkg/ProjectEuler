# Copyright 2019 fssqawj Holding Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http,//www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from copy import deepcopy


data = [
    ("5616185650518293", 2),
    ("3847439647293047", 1),
    ("5855462940810587", 3),
    ("9742855507068353", 3),
    ("4296849643607543", 3),
    ("3174248439465858", 1),
    ("4513559094146117", 2),
    ("7890971548908067", 3),
    ("8157356344118483", 1),
    ("2615250744386899", 2),
    ("8690095851526254", 3),
    ("6375711915077050", 1),
    ("6913859173121360", 1),
    ("6442889055042768", 2),
    ("2321386104303845", 0),
    ("2326509471271448", 2),
    ("5251583379644322", 2),
    ("1748270476758276", 3),
    ("4895722652190306", 1),
    ("3041631117224635", 3),
    ("1841236454324589", 3),
    ("2659862637316867", 2)
]

# data = sorted(data, key=lambda x: x[1], reverse=True)
# print(data)

# data = [
#     ("90342", 2),
#     ("70794", 0),
#     ("39458", 2),
#     ("34109", 1),
#     ("51545", 2),
#     ("12531", 1)
# ]


def matched(item, current):
    res = []
    for idx, (x, y) in enumerate(zip(item, current)):
        if x == y:
            res.append(idx)
    return res


def gen(ids, cnt):
    res = []

    def _subset(cur, target):
        # print(cur, target)
        if len(target) == cnt:
            res.append(deepcopy(target))
            return
        for idx in range(cur + 1, len(ids)):
            target.append(ids[idx])
            _subset(idx, target)
            target.pop(-1)

    _subset(-1, [])

    return res


def check(current):
    if any([x == -1 for x in current]):
        return False
    # print(current)
    # for item, cnt in data:
    #     print(item, matched(item, current), cnt)
    return all([len(matched(item, current)) == cnt for item, cnt in data])


def pre_check(current):
    for item, cnt in data:
        if len(matched(item, current)) > cnt:
            return False
    return True


def solve(idx, current):
    if idx >= 20:
        print(idx, "".join([str(x) for x in current]))
    if idx == len(data):
        if check(current):
            print("".join(current))
        return
    item, cnt = data[idx]
    if not pre_check(current):
        return
    match_idx = matched(item, current)
    if len(match_idx) > cnt:
        return
    ids = [x for x in range(len(item)) if current[x] == -1]
    if len(ids) < cnt - len(match_idx):
        return
    if len(ids) == 0 or cnt == len(match_idx):
        solve(idx + 1, current)
    else:
        for term in gen(ids, cnt - len(match_idx)):
            for i in term:
                current[i] = item[i]
            solve(idx + 1, current)
            for i in term:
                current[i] = -1


def main():
    solve(0, [-1 for _ in range(len(data[0][0]))])
    # print(gen([1,2,3], 3))


if __name__ == '__main__':
    main()


# 22 ['4', '6', '4', '0', '2', '6', '1', '5', '7', '1', '8', '4', -1, '5', '3', '3'] add "9" at last 4-th
