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
from itertools import permutations

if __name__ == '__main__':
    res = 0
    for item in permutations(range(10)):
        item = list(item)
        if int(''.join(str(x) for x in item[1:4])) % 2 == 0 \
                and int(''.join(str(x) for x in item[2:5])) % 3 == 0 \
                and int(''.join(str(x) for x in item[3:6])) % 5 == 0 \
                and int(''.join(str(x) for x in item[4:7])) % 7 == 0 \
                and int(''.join(str(x) for x in item[5:8])) % 11 == 0 \
                and int(''.join(str(x) for x in item[6:9])) % 13 == 0 \
                and int(''.join(str(x) for x in item[7:10])) % 17 == 0:
            print(item)
            res += int(''.join(str(x) for x in item))
    print(res)
