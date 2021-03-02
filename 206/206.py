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

from utils import is_square


def find(idx, res):
    if idx == 8:
        res = res * 1000 + 900
        # print(res)
        if is_square(res):
            print(res)
        return
    for i in range(10):
        t_res = res * 100 + (idx + 1) * 10 + i
        find(idx + 1, t_res)


if __name__ == '__main__':
    # find(0, 0)
    print(math.sqrt(1929374254627488900))
