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


father = list(range(40))


def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]


def union(x, y):
    fx, fy = find(x), find(y)
    father[fy] = fx


if __name__ == '__main__':
    with codecs.open('p107_network.txt', 'r', encoding='utf-8') as fin:
        edges = []
        for idx, line in enumerate(fin):
            line = [int(x) if x != '-' else 1e11 for x in line.strip().split(",")]
            for j in range(idx + 1, len(line)):
                edges.append((idx, j, line[j]))
        edges = sorted(edges, key=lambda x: x[2])
        all_len = sum([x[2] for x in edges if x[2] != 1e11])
        res = 0
        for edge in edges:
            rx, ry = find(edge[0]), find(edge[1])
            if rx != ry:
                res += edge[2]
                union(rx, ry)
        print(res, all_len - res)
