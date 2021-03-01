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
import pickle


if __name__ == '__main__':
    # data = pickle.load(open('/Users/anweijie/Documents/primes_2_billion.set', 'rb'))

    edges = [0, 1]

    tem = 2
    for i in range(1000):
        edges.append(tem + i * 6)
        tem = edges[-1]

    cur_idx = 2
    cur_cycle = 2

    cnt = 1

    while True:
        cur_begin = edges[cur_cycle]
        pre_begin = edges[cur_cycle - 1]
        nex_begin = edges[cur_cycle + 1]



