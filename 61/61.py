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
import itertools


vis = [False for _ in range(5)]


def find(nums, res):
    if len(nums) == 6:
        if nums[-1] % 100 == nums[0] // 100:
            print(nums, sum(nums))
        return
    last = nums[-1]
    for i in range(5):
        if not vis[i]:
            for num in res[i]:
                if last % 100 == num // 100 and num not in nums:
                    vis[i] = True
                    nums.append(num)
                    find(nums, res)
                    nums.remove(num)
                    vis[i] = False


if __name__ == '__main__':
    p_3 = [x * (x + 1) // 2 for x in range(200) if 10000 > x * (x + 1) // 2 > 1000]
    p_4 = [x * x for x in range(200) if 10000 > x * x > 1000]
    p_5 = [x * (3 * x - 1) // 2 for x in range(200) if 10000 > x * (3 * x - 1) // 2 > 1000]
    p_6 = [x * (4 * x - 2) // 2 for x in range(200) if 10000 > x * (4 * x - 2) // 2 > 1000]
    p_7 = [x * (5 * x - 3) // 2 for x in range(200) if 10000 > x * (5 * x - 3) // 2 > 1000]
    p_8 = [x * (6 * x - 4) // 2 for x in range(200) if 10000 > x * (6 * x - 4) // 2 > 1000]

    res = [p_4, p_5, p_6, p_7, p_8]

    for num in p_3:
        find([num], res)


