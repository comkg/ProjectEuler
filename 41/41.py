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
from utils import is_prime


numbers = []


def get_number(nums):
    res = 0
    for num in nums:
        res = res * 10 + num
    return res


def get_all_numbers(pre_numbers):
    if len(pre_numbers) == 7:
        numbers.append(get_number(pre_numbers))
        return
    for i in range(1, 8):
        if i not in pre_numbers:
            pre_numbers.append(i)
            get_all_numbers(pre_numbers)
            pre_numbers.remove(i)


if __name__ == '__main__':
    get_all_numbers([])
    for number in numbers:
        if is_prime(number):
            print(number)
