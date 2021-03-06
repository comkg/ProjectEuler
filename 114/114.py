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


res = {}


def find(n, m):
    cnt = 1
    if m > n:
        return cnt
    if n in res:
        return res[n]
    for pos in range(n - m + 1):
        for block_len in range(m, n - pos + 1):
            cnt += find(n - pos - block_len - 1, m)
    res[n] = cnt
    return res[n]


if __name__ == '__main__':
    i = 50
    while find(i, 50) <= 1000000:
        print(i)
        i += 1

