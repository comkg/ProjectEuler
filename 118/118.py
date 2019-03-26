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
from utils import get_all_prime
import pickle as pkl
from itertools import permutations, combinations
from tqdm import tqdm


def to_int(x):
    res = 0
    for dig in x:
        res = res * 10 + dig
    return res


def get_part_list(items, pos):
    res = []
    for i in range(1, len(pos)):
        res.append(to_int(items[pos[i - 1]:pos[i]]))
    return res


if __name__ == '__main__':
    # primes_set = set(get_all_prime(10 ** 9))
    # pkl.dump(primes_set, open('primes.set', 'wb'))
    primes = pkl.load(open('primes.set', 'rb'))
    res = 0
    judge_set = set()
    for item in tqdm(permutations(range(1, 10), 9)):
        for part in range(2, 7):
            for pos in combinations(range(1, 9), part - 1):
                pos_list = [0] + list(pos) + [9]
                item_list = list(item)
                part_list = sorted(get_part_list(item_list, pos_list))
                # print(part_list)
                key = '#'.join([str(x) for x in part_list])
                if key in judge_set:
                    continue
                judge_set.add(key)
                if all([x in primes for x in part_list]):
                    # print(part_list)
                    res += 1
    print(res)
