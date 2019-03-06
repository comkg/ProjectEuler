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
from itertools import permutations, combinations
from tqdm import tqdm


def is_int(x):
    return x > 0 and abs(x - int(x)) < 1e-5


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


operations = [add, sub, mul, div]


def calc(terms, idx, res, vis):
    if idx == len(terms):
        if is_int(res):
            vis.add(int(res))
        return

    calc(terms, idx + 1, res + terms[idx], vis)
    calc(terms, idx + 1, res - terms[idx], vis)
    calc(terms, idx + 1, res * terms[idx], vis)
    calc(terms, idx + 1, res / terms[idx], vis)


def double_calc(terms, stage, vis):
    if len(stage) == 3:
        tem = stage[1](stage[0](terms[0], terms[1]), stage[2](terms[2], terms[3]))
        if is_int(tem):
            vis.add(int(tem))
        return
    for op in operations:
        stage.append(op)
        double_calc(terms, stage, vis)
        stage.remove(op)


if __name__ == '__main__':
    res = 0
    ans = None
    for xerms in tqdm(combinations([x for x in range(1, 10)], 4)):
        vis = set()
        for terms in permutations(xerms):
            calc(terms, 1, terms[0], vis)
            double_calc(terms, [], vis)
        tem = 1
        while tem in vis:
            tem += 1
        if tem > res:
            ans = xerms
            res = tem
    print(res, ans)
