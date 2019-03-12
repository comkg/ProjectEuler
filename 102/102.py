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
    with codecs.open('p102_triangles.txt', 'r', encoding='utf-8') as fin:
        res = 0
        for line in fin.readlines():
            line = [int(x) for x in line.strip().split(",")]
            # print(line)
            a = line[0] * line[3] - line[1] * line[2]
            b = line[2] * line[5] - line[3] * line[4]
            c = line[4] * line[1] - line[5] * line[0]
            # print(a, b, c)
            if a * b > 0 and a * c > 0:
                # print(line)
                res += 1
        print(res)
