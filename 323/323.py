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
import math


if __name__ == '__main__':
    eps = 1e-11
    res = 0
    cnt = 0
    while cnt < 80:
        tem = math.pow(1 - math.pow(0.5, cnt), 32)

        if 1 - tem < eps:
            break

        print(cnt, tem)
        res += (1 - tem)
        cnt += 1
    print(res)
