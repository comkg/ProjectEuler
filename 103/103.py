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


def is_rule_1(numbers):
    sub_sets = set()
    for i in range(1, 1 << (len(numbers))):
        tem = 0
        for j in range(0, len(numbers)):
            if (i >> j) & 1:
                tem += numbers[j]
        if tem in sub_sets:
            return False
        sub_sets.add(tem)
    return True


def is_rule_2(numbers):
    for i in range(2, (len(numbers) + 1) // 2 + 1):
        if sum(numbers[:i]) <= sum(numbers[-i + 1:]):
            return False
    return True


res = 1e11
res_str = None


def find(numbers, target):
    if len(numbers) == target:
        if is_rule_1(numbers) and is_rule_2(numbers):
            global res, res_str
            if sum(numbers) < res:
                res = sum(numbers)
                res_str = ' '.join([str(x) for x in numbers])
                print(res, res_str)
        return
    for i in range(numbers[-1] + 1, sum(numbers[:2]) if len(numbers) > 1 else 2 * numbers[-1] + 1):
        numbers.append(i)
        find(numbers, target)
        numbers.pop()


if __name__ == '__main__':
    find([20], 7)
    # print(res, res_str)
