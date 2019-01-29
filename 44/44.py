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


if __name__ == '__main__':
    n = 10000
    numbers = [x * (3 * x - 1) // 2 for x in range(1, n)]
    numbers_set = set(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if numbers[i] + numbers[j] in numbers_set and numbers[j] - numbers[i] in numbers_set:
                print(i, j, numbers[i], numbers[j])
                print(numbers[j] - numbers[i])
