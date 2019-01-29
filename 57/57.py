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
from utils import gcd

import sys
sys.setrecursionlimit(100000)


if __name__ == '__main__':
    pre = 0, 1
    cnt = 0
    res = 0
    while cnt < 1000:
        tem = pre[1], 2 * pre[1] + pre[0]
        print(tem)
        div = gcd(tem[1], tem[0] + tem[1])
        if len(str((tem[0] + tem[1]) // div)) > len(str(tem[1] // div)):
            res += 1
        div = gcd(tem[0], tem[1])
        pre = tem[0] // div, tem[1] // div
        cnt += 1
    print(res)
