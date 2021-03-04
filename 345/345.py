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
from tqdm import tqdm


class KM(object):
    def __init__(self, edges, n, m):
        self._edges = edges
        self._n = n
        self._m = m
        self._link = [-1 for _ in range(m)]
        self._val_x = [0 for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self._val_x[i] = max(self._val_x[i], edges[i][j])
        self._val_y = [0 for _ in range(m)]
        self._vis_x = [False for _ in range(n)]
        self._vis_y = [False for _ in range(m)]

    def find_path(self, x):
        self._vis_x[x] = True
        for y in range(self._m):
            if not self._vis_y[y] \
                    and self._val_x[x] + self._val_y[y] == self._edges[x][y]:
                self._vis_y[y] = True
                if self._link[y] == -1 or self.find_path(self._link[y]):
                    self._link[y] = x
                    return True
        return False

    def max_math(self):
        for i in range(self._n):
            while True:
                self._vis_x = [False for _ in range(self._n)]
                self._vis_y = [False for _ in range(self._m)]
                if self.find_path(i):
                    break
                d = -1
                for x in range(self._n):
                    if self._vis_x[x]:
                        for y in range(self._m):
                            if not self._vis_y[y]:
                                tem_d = self._val_x[x] + self._val_y[y]\
                                        - self._edges[x][y]
                                if d == -1:
                                    d = tem_d
                                else:
                                    d = min(d, tem_d)
                if d == -1:
                    return -1
                for x in range(self._n):
                    if self._vis_x[x]:
                        self._val_x[x] -= d
                for y in range(self._m):
                    if self._vis_y[y]:
                        self._val_y[y] += d
            print(self._link)
        res = 0
        for i in range(self._m):
            res += self._edges[self._link[i]][i]
            print(self._link[i], i, self._edges[self._link[i]][i], res)
        return res


def load_data(file_path):
    res = []
    with open(file_path, "r") as fin:
        for line in fin:
            line = [int(x) for x in line.strip().split(" ") if len(x) > 0]
            res.append(line)
    return res


def main():
    # file_path = "345/sample.txt"
    file_path = "345/test.txt"
    data = load_data(file_path)
    km = KM(data, len(data), len(data[0]))
    res = km.max_math()
    print(res)


if __name__ == '__main__':
    main()
