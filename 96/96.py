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


res = 0


def solve(p, idx, pads, tx, ty):
    # print(tx, ty)
    # print(p)
    # global res
    # if res == 0:
    #     return
    # res -= 1
    # print(idx)
    if idx == len(pads):
        global res
        # print(p)
        res += p[0][0] * 100 + p[0][1] * 10 + p[0][2]
        print(res)
        return
    i, j = pads[idx]
    rows = [p[x][j] for x in range(9)]
    cols = [p[i][x] for x in range(9)]
    # print("i: ", i, " j: ", j)
    # print("rows", rows)
    # print("cols", cols)
    upper = i // 3
    left = j // 3
    # print(upper, left)
    grids = [p[x][y] for x in range(upper * 3, upper * 3 + 3) for y in range(left * 3, left * 3 + 3)]
    # print("grids", grids)
    for tem in range(1, 10):
        if tem not in set(rows + cols + grids):
            # print(i, j, tem)
            p[i][j] = tem
            solve(p, idx + 1, pads, i, j)
            p[i][j] = 0


if __name__ == '__main__':
    with codecs.open('p096_sudoku.txt', 'r', encoding='utf-8') as fin:
        tem = [[0] * 9] * 9
        for idx, line in enumerate(fin):
            if idx % 10 == 0:
                if idx != 0:
                    pads = []
                    for i in range(9):
                        for j in range(9):
                            if tem[i][j] == 0:
                                pads.append((i, j))
                    solve(tem, 0, pads, -1, -1)
                    # break
                    # print(tem)
                continue
            tem[idx % 10 - 1] = [int(x) for x in line.strip()]
