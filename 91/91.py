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


if __name__ == '__main__':
    res = 0
    for a in range(1, 51 * 51):
        for b in range(a + 1, 51 * 51):
            a_x, a_y = a // 51, a % 51
            b_x, b_y = b // 51, b % 51
            if a_x * b_y == b_x * a_y:
                continue
            l = sorted([a_x * a_x + a_y * a_y, b_x * b_x + b_y * b_y,
                        (a_x - b_x) * (a_x - b_x) + (a_y - b_y) * (a_y - b_y)])
            if l[0] + l[1] == l[2]:
                res += 1
    print(res)
