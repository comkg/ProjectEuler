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


vis = {x: -1 for x in range(12001)}

cnt = 0


def calc(divs, num, origin):
    # print(divs, num, origin)
    if num == 1:
        k = origin - sum(divs) + len(divs)
        if k > 12000 or k < 2:
            return
        if vis[k] == -1:
            print(k, origin)
            vis[k] = origin
            global cnt
            cnt += 1
            return
        return
    for i in range(2, num + 1):
        if num % i == 0:
            divs.append(i)
            calc(divs, num // i, origin)
            del divs[-1]


if __name__ == '__main__':
    i = 4
    while cnt < 11999:
        calc([], i, i)
        i += 1
        # break
    nums = set()
    for key in vis:
        if vis[key] != -1:
            nums.add(vis[key])
        else:
            print(key)
    print(sum(nums))
