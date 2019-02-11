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
    dp = []
    with codecs.open('p081_matrix.txt', 'r', encoding='utf-8') as fin:
        for idx, line in enumerate(fin):
            line = line.strip().split(',')
            tem = []
            for jdx, item in enumerate(line):
                item = int(item)
                if idx == 0 and jdx == 0:
                    tem.append(item)
                elif idx == 0:
                    tem.append(item + tem[-1])
                elif jdx == 0:
                    tem.append(item + dp[-1][0])
                else:
                    tem.append(min(dp[-1][jdx], tem[-1]) + item)
            dp.append(tem)
        print(dp[-1][-1])
