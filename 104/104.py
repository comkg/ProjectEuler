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


def valid(x):
    return len(set(x)) == 9 and '0' not in x


if __name__ == '__main__':
    pre_a, pre_b = 1, 1
    cnt = 3
    while True:
        tem = pre_a + pre_b
        pre_a = pre_b
        pre_b = tem
        tem = str(tem)
        if valid(tem[:9]) and valid(tem[-9:]):
            print(cnt, tem)
            break
        cnt += 1
        if cnt % 10000 == 0:
            print(cnt)