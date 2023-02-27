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


res = 0


def solve(idx, current, digits):
    if idx == 20:
        if current % 11 == 0:
            print(current, current // 11)
            global res
            res += 1
        return
    for i in range(9, -1 if idx > 0 else 0, -1):
        if digits[i] < 2:
            digits[i] += 1
            solve(idx + 1, current * 10 + i, digits)
            digits[i] -= 1


def main():
    solve(0, 0, {i: 0 for i in range(10)})
    print(res)


if __name__ == '__main__':
    main()
