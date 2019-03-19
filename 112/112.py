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


def is_valid(x):
    if len(x) < 3:
        return True
    for i in range(1, len(x)):
        if x[i] < x[i - 1]:
            return False
    return True


if __name__ == '__main__':
    cnt = 0
    n = 539
    i = 1
    while True:
        tem = str(i)
        if is_valid(tem) or is_valid(tem[::-1]):
            print(i)
            cnt += 1
        print(cnt, cnt / i)
        if cnt / i == 0.01:
            print(i)
            break
        i += 1
    # print(cnt, cnt / (n - 1))
