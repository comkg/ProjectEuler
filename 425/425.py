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
from queue import PriorityQueue

from utils import get_all_prime


def main():
    n = 10 ** 7
    primes = set(get_all_prime(n))
    print(len(primes))
    connected = [0 for _ in range(n)]
    tem_q = PriorityQueue()
    tem_q.put(2)
    connected[2] = 2
    while not tem_q.empty():
        c_p = tem_q.get()
        # print(cur_idx, c_p)
        c_p_str = str(c_p)
        for idx in range(len(c_p_str)):
            for c in range(1 if idx == 0 else 0, 10, 1):
                if str(c) == c_p_str[idx]:
                    continue
                t_c_p = int(c_p_str[:idx] + str(c) + c_p_str[idx + 1:])
                if t_c_p in primes:
                    if connected[t_c_p] == 0:
                        tem_q.put(t_c_p)
                        connected[t_c_p] = max(t_c_p, connected[c_p])
                    else:
                        t_max = max(t_c_p, connected[c_p])
                        if t_max < connected[t_c_p]:
                            tem_q.put(t_c_p)
                            connected[t_c_p] = t_max
                    # print(c_p, t_c_p, connected[t_c_p])
        for i in range(1, 10, 1):
            a_p = int(str(i) + c_p_str)
            if a_p in primes:
                if connected[a_p] == 0:
                    tem_q.put(a_p)
                    connected[a_p] = max(a_p, connected[c_p])
                else:
                    t_max = max(a_p, connected[c_p])
                    if t_max < connected[a_p]:
                        tem_q.put(a_p)
                        connected[a_p] = t_max

        a_p = 0 if len(c_p_str) == 1 or c_p_str[1] == "0" else int(c_p_str[1:])
        if a_p in primes:
            if connected[a_p] == 0:
                tem_q.put(a_p)
                connected[a_p] = max(a_p, connected[c_p])
                print(c_p, a_p, connected[a_p])
            else:
                t_max = max(a_p, connected[c_p])
                if t_max < connected[a_p]:
                    tem_q.put(a_p)
                    connected[a_p] = t_max

            # a_p = int(str(c_p) + str(i))
            # if a_p in primes:
            #     if connected[a_p] == 0:
            #         tem_q.append(a_p)
            #         connected[a_p] = max(a_p, connected[c_p])
            #     else:
            #         t_max = max(a_p, connected[c_p])
            #         if t_max < connected[a_p]:
            #             tem_q.append(a_p)
            #             connected[a_p] = t_max
            #     print(c_p, a_p, connected[a_p])
    # print(connected)
    # print(tem_q)
    res = 0
    for prime in primes:
        if connected[prime] > prime or connected[prime] == 0:
            print(prime)
            res += prime
    print(res)


if __name__ == '__main__':
    main()
