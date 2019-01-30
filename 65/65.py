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


if __name__ == '__main__':
    nums = [2]
    for i in range(1, 34):
        nums.append(1)
        nums.append(2 * i)
        nums.append(1)
    upper = nums[-1]
    lower = 1
    for i in range(98, -1, -1):
        t_up = nums[i] * upper + lower
        t_low = upper
        div = gcd(t_up, t_low)
        upper = t_up // div
        lower = t_low // div
        print(upper, lower, upper / lower, sum([int(x) for x in str(upper)]))
