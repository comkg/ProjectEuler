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


def main():
    res = 1
    cnt = 0
    n = 1777
    # print(62690417 * n)
    hap = set()
    while True:
        res = (res * n) % 4
        cnt += 1
        print(res)
        print(cnt)
        if res in hap:
            break
        hap.add(res)


def _pow(x, n, m):
    res = 1
    for _ in range(n):
        res = (res * x) % m
    return res


if __name__ == '__main__':
    # main()
    print(_pow(1777, 962097, 100000000))
    # 1855, 100000000, 1777 ** 962097 % 100000000 = 95962097
    # 1854, 1250000, 1777 ** 24597 % 1250000 = 962097
    # 1853, 62500, 1777 ** 12097 % 62500 = 24597
    # 1852, 12500, 1777 ** 2097 % 12500 = 12097
    # 1851, 2500, 1777 ** 97 % 2500 = 2097
    # 1850, 500, 1777 ** 97 % 500 = 97
    # 1849, 100, 1777 ** 17 % 100 = 97
    # 1848, 20, 1777 * 1 % 20 = 17
    # 1847, 4, 1
