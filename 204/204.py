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
from tqdm import tqdm


def get_all_prime(n, m):
    res = 0
    prime = [1 for _ in range(n)]
    for i in tqdm(range(2, n)):
        if prime[i] == 1:
            for j in range(i, n, i):
                if i > m >= prime[j]:
                    res += 1
                prime[j] = i
    return res


if __name__ == '__main__':
    # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
    n, m = 10 ** 9 + 1, 100
    res = get_all_prime(n, m)
    print(res)
    print(n - res - 1)
