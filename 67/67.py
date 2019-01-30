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


if __name__ == '__main__':
    with codecs.open('p067_triangle.txt', 'r', encoding='utf-8') as fin:
        res = []
        for idx, line in enumerate(fin):
            line = line.strip().split()
            if idx == 0:
                res.append([int(x) for x in line])
                continue
            tem = []
            for j in range(idx):
                if j == 0:
                    tem.append(int(line[j]) + res[idx - 1][0])
                elif j == idx - 1:
                    tem.append(int(line[j]) + res[idx - 1][j - 1])
                else:
                    tem.append(max(res[idx - 1][j - 1], res[idx - 1][j]) + int(line[j]))
            res.append(tem)
        print(max(res[-1]))
