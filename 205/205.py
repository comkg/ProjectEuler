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


def find(idx, target, dice_num, tem_sum, res):
    if idx == target:
        res[tem_sum] = res.get(tem_sum, 0) + 1
        return
    for i in range(1, dice_num + 1):
        find(idx + 1, target, dice_num, tem_sum + i, res)


if __name__ == '__main__':
    res_4 = {}
    find(0, 9, 4, 0, res_4)
    total = sum(res_4.values())
    res_4 = {x: res_4[x] / total for x in res_4}
    res_6 = {}
    find(0, 6, 6, 0, res_6)
    total = sum(res_6.values())
    res_6 = {x: res_6[x] / total for x in res_6}
    print(res_4)
    print(res_6)
    res = 0
    for item in res_4:
        for jtem in res_6:
            if item > jtem:
                res += res_4[item] * res_6[jtem]
    print(res)
