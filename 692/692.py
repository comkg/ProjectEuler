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


def find():
    res = {0: 0, 1: 1}
    n = 405
    target = 1
    pre_idx = target
    cnt = {1: 1}
    for i in range(2, n, 1):
        pre = i // 3
        for j in range(1, pre + 1, 1):
            if res[i - j] > j * 2:
                res[i] = j
                break
        else:
            res[i] = i
        # if res[i] == target:
        #     cnt[i - pre_idx] = cnt.get(i - pre_idx, 0) + 1
        cnt[i] = cnt[i - 1] + res[i]
        print(i, res[i], cnt[i])

        #     pre_idx = i
    # print(cnt)


def main():
    res = {1: 1}
    s_pre = 1
    pre = 1
    cur = 2
    n = 23416728348467685
    # n = 400
    while cur <= n:
        res[cur] = res[pre] + res[s_pre] - s_pre + cur
        print(cur, res[cur])
        s_pre = pre
        t_pre = pre
        pre = cur
        cur = cur + t_pre
        # print(s_pre, pre, cur)
    rt = 0
    while n > 0:
        target = -1
        for item in res:
            if item <= n:
                target = max(target, item)
        rt += res[target]
        n -= target
    print(rt)


if __name__ == '__main__':
    # find()
    main()

    # 1: 1
    # 2: 2
    # 3: 3
    # 4: 1
    # 5: 5
    # 6: 1
    # 7: 2
    # 8: 8
    # 9: 1
    # 10: 2
    # 11: 3
    # 12: 1
    # 13: 13
    # 14: 1
    # 15: 2
    # 16: 3
    # 17: 1
    # 18: 5
    # 19: 1
    # 20: 2
    # 21: 21
    # 22: 1
    # 23: 2
    # 24: 3
    # 25: 1
    # 26: 5
    # 27: 1
    # 28: 2
    # 29: 8
    # 30: 1
    # 31: 2
    # 32: 3
    # 33: 1
    # 34: 34
    # 35: 1
    # 36: 2
    # 37: 3
    # 38: 1
    # 39: 5
    # 40: 1
    # 41: 2
    # 42: 8
    # 43: 1
    # 44: 2
    # 45: 3
    # 46: 1
    # 47: 13
    # 48: 1
    # 49: 2
    # 50: 3
    # 51: 1
    # 52: 5
    # 53: 1
    # 54: 2
    # 55: 55
    # 56: 1
    # 57: 2
    # 58: 3
    # 59: 1
    # 60: 5

