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
import math
from utils import is_square


def main():
    cur = 1
    cnt = 0
    res = 0
    while True:
        if is_square(5 * cur * cur + 4 * cur + 1):
            cnt += 1
            res += math.sqrt(5 * cur * cur + 4 * cur + 1)
            print(cur, 2 * cur + 1, math.sqrt(5 * cur * cur + 4 * cur + 1),
                  cnt, res, "0")
        if is_square(5 * cur * cur - 4 * cur + 1):
            cnt += 1
            res += math.sqrt(5 * cur * cur - 4 * cur + 1)
            print(cur, 2 * cur - 1, math.sqrt(5 * cur * cur - 4 * cur + 1),
                  cnt, res, "1")
        if cnt == 12:
            break
        # print(cur)
        cur += 1

    print(res)


def fib():
    cur = 1
    pre = 1
    cnt = 40
    while cnt > 0:
        _cur = cur
        cur = cur + pre
        pre = _cur
        print(cur, cur / pre)
        cnt -= 1


if __name__ == '__main__':
    # fib()
    # main()
    cur = 1
    cnt = 0
    res = 0
    while True:
        target = int(cur * (9 + math.sqrt(5) * 4))
        print(target, math.sqrt(5 * target * target - 1))
        res += target
        cur = target
        cnt += 1
        if cnt == 12:
            break
        # while target > 0:
        #     # print(target)
        #     if is_square(5 * target * target - 1):
        #         print(target, math.sqrt(5 * target * target - 1))
        #         break
        #     target += 1
        # cur = target
    print(res)
