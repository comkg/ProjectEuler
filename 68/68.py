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
from utils import permutations


def judge(pool):
    for i in range(1, 5):
        if pool[i] != pool[0]:
            return False
    return True


if __name__ == '__main__':
    res = 0
    for item in permutations([x for x in range(1, 11)]):
        if 10 in list(item)[:5]:
            continue
        pool = [item[5] + item[0] + item[1],
                item[6] + item[1] + item[2],
                item[7] + item[2] + item[3],
                item[8] + item[3] + item[4],
                item[9] + item[4] + item[0],
                ]
        if judge(pool):
            a1 = int(str(item[5]) + str(item[0]) + str(item[1]))
            a2 = int(str(item[6]) + str(item[1]) + str(item[2]))
            a3 = int(str(item[7]) + str(item[2]) + str(item[3]))
            a4 = int(str(item[8]) + str(item[3]) + str(item[4]))
            a5 = int(str(item[9]) + str(item[4]) + str(item[0]))
            if min(a1, a2, a3, a4, a5) == a1:
                tem = int(''.join([str(x) for x in [item[5], item[0], item[1],
                                                    item[6], item[1], item[2],
                                                    item[7], item[2], item[3],
                                                    item[8], item[3], item[4],
                                                    item[9], item[4], item[0],]]))
                res = max(tem, res)
                print(res)
    print(res)
