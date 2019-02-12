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
from utils import is_square


if __name__ == '__main__':
    def calc(t):
        res = 0
        for j in range(1, t + 1):
            for k in range(1, j + 1):
                if is_square(t * t + (j + k) * (j + k)):
                    res += 1
        return res
    res = 0
    for i in range(1, 2000):
        res += calc(i)
        print(i, res)
        if res > 1000000:
            print(res)
            break
    # l, r = 1000, 2000
    # res = -1
    # while l <= r:
    #     mid = (l + r) // 2
    #     tem = calc(mid)
    #     print(tem, mid)
    #     if tem > 1000000:
    #         res = mid
    #         r = mid - 1
    #     else:
    #         l = mid + 1
    # print(res)
