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


res = [-1 for i in range(10000000)]
res[1] = 1
res[89] = 89


def find(x):
    if res[x] != -1:
        return res[x]
    if x == 1:
        return 1
    if x == 89:
        return 89
    return find(sum([int(i) ** 2 for i in str(x)]))


if __name__ == '__main__':
    cnt = 0
    for i in range(2, 10000000):
        res[i] = find(i)
        print(i, res[i])
        if res[i] == 89:
            cnt += 1
    print(cnt)
