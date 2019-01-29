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
    n = 1000000 - 1
    res = 0
    numbers = list(range(0, 10))
    for i in range(9, -1, -1):
        num = n // math.factorial(i)
        n -= num * math.factorial(i)
        print(num, n)
        res = res * 10 + numbers[num]
        numbers.remove(numbers[num])

    print(res)
