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
from utils import euler_func


if __name__ == '__main__':
    res = 1e11
    for i in range(6, 10000000):
        # print(i)
        tem = euler_func(i)
        if sorted(str(tem)) == sorted(str(i)):
            if res > i / tem:
                res = i / tem
                print(i, tem, res)
