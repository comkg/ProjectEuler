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


if __name__ == '__main__':
    print(count(4, 2))
    target = 1000000
    res = 0
    length = target // 4 + 1
    while length > 0:
        l, r = 1, (length - 1) // 2 + 1
        res_t = 0
        while l <= r:
            mid = (l + r) // 2
            if count(length, mid) > target:
                r = mid - 1
            else:
                l = mid + 1
                res_t = mid
        res += res_t
        print(length, res_t, res)
        length -= 1
    print(res)
