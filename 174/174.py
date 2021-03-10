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
from tqdm import tqdm


def count(n, m):
    if m > (n - 1) // 2:
        return 1e11
        # raise Exception("invalid params for n: {}, m: {}".format(n, m))
    # res = 0
    # while m > 0:
    #     res += 4 * n - 4
    #     res += 1 if n == 1 else 0
    #     m -= 1
    #     n -= 2
    # return res
    return 4 * m * n - 4 * m - 4 * m * (m - 1)


def main():
    target = 1000000
    length = target // 4 + 1
    res = {}
    for i in tqdm(range(length, 2, -1)):
        m = 1
        while True:
            used = count(i, m)
            print(i, m, used)
            if used <= target:
                res[used] = res.get(used, 0) + 1
            else:
                break
            m += 1
    rt = 0
    for item in res:
        if 1 <= res[item] <= 10:
            print(item)
            rt += 1
    print(rt)


if __name__ == '__main__':
    main()
