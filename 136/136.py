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

#
# def satisfy(tx):
#     cnt = 0
#     for i in range(1, int(math.sqrt(tx + 1)) + 1):
#         if tx % i == 0:
#             p = i
#             q = tx // i
#             px, qx = -1, -1
#             # print(p, q)
#             if (p + q) % 4 == 0 and ((5 * p + q) % 4 == 0 or (p + 5 * q) % 4 == 0):
#                 if (5 * p + q) % 4 == 0:
#                     px = (5 * p + q) // 4
#                     k = (p + q) // 4
#                     if px - 2 * k > 0:
#                         cnt += 1
#                     # tem = px ** 2 - (px - k) ** 2 - (px - 2 * k) ** 2
#                     # print(p, q, px, px - k, px - 2 * k, tem)
#                 if (p + 5 * q) % 4 == 0:
#                     qx = (p + 5 * q) // 4
#                     k = (p + q) // 4
#                     if qx - 2 * k > 0:
#                         cnt += 1
#                     # tem = qx ** 2 - (qx - k) ** 2 - (qx - 2 * k) ** 2
#                     # print(p, q, qx, qx - k, qx - 2 * k, tem)
#                 if px == qx and px != -1:
#                     cnt -= 1
#                 # tem = x ** 2 - (x - k) ** 2 - (x - 2 * k) ** 2
#                 # print(p, q, x, x - k, x - 2 * k, tem)
#                 # cnt += 1
#     # if cnt == 1:
#     #     print("gold")
#     # else:
#     #     print("bad")
#     return cnt == 1


if __name__ == '__main__':
    n = 50000000
    res = {}
    for p in range(1, n + 1):
        print(p)
        q = p
        while p * q <= n:
            cnt = 0
            px, qx = -1, -1
            if (p + q) % 4 == 0 and ((5 * p + q) % 4 == 0 or (p + 5 * q) % 4 == 0):
                if (5 * p + q) % 4 == 0:
                    px = (5 * p + q) // 4
                    k = (p + q) // 4
                    if px - 2 * k > 0:
                        cnt += 1
                    # tem = px ** 2 - (px - k) ** 2 - (px - 2 * k) ** 2
                    # print(p, q, px, px - k, px - 2 * k, tem)
                if (p + 5 * q) % 4 == 0:
                    qx = (p + 5 * q) // 4
                    k = (p + q) // 4
                    if qx - 2 * k > 0:
                        cnt += 1
                    # tem = qx ** 2 - (qx - k) ** 2 - (qx - 2 * k) ** 2
                    # print(p, q, qx, qx - k, qx - 2 * k, tem)
                if px == qx and px != -1:
                    cnt -= 1
            res[p * q] = res.get(p * q, 0) + cnt
            q += 1
    cnt = 0
    for item in res:
        if res[item] == 1:
            print(item)
            cnt += 1
    print(cnt)
