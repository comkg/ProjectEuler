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


def phi(n):
    res = [0 for _ in range(n)]
    vis = [False for _ in range(n)]
    primes = []
    for i in range(2, n):
        if not vis[i]:
            vis[i] = True
            primes.append(i)
            res[i] = i - 1
        j = 0
        while j < len(primes) and i * primes[j] < n:
            k = i * primes[j]
            vis[k] = True
            if i % primes[j] == 0:
                res[k] = res[i] * primes[j]
                break
            else:
                res[k] = res[i] * (primes[j] - 1)
            j += 1
    return res


if __name__ == '__main__':
    res = 0
    eulers = phi(1000001)
    print(eulers)
    for i in range(2, 1000001):
        res += eulers[i]
    print(res)
