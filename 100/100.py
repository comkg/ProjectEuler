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
from utils import is_square


if __name__ == '__main__':
    x1, y1 = 3, 2
    pre_x, pre_y = x1, y1
    cnt = 0
    while True:
        tem_x, tem_y = x1 * pre_x + 2 * y1 * pre_y, x1 * pre_y + pre_x * y1
        tar_x, tar_y = 41 * tem_x + 58 * tem_y, 41 * tem_y + 29 * tem_x
        if tar_y % 2 == 1:
            x = (tar_y + 1) // 2
            if (1 - 2 * x + tar_x) % 2 == 0:
                y = (1 - 2 * x + tar_x) // 2
                print(x, y, x * (x - 1) / ((x + y) * (x + y - 1)), x + y)
                if x + y > 1000000000000:
                    break
        # print(tem_x, tem_y, tar_x * tar_x - 2 * tar_y * tar_y)
        pre_x, pre_y = tem_x, tem_y
