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
    # it is a little hard... ref https://www.mathblog.dk/project-euler-126-cubes-cover-cuboid/
    def find(x, y, z, n):
        return 2 * (x * y + y * z + z * x) + 4 * (x + y + z + n - 2) * (n - 1)
    limit = 30000
    res = {}
    for i in range(1, limit):
        if find(i, i, i, 1) > limit:
            break
        for j in range(i, limit):
            if find(i, j, j, 1) > limit:
                break
            for k in range(j, limit):
                if find(i, j, k, 1) > limit:
                    break
                for n in range(1, limit):
                    if find(i, j, k, n) > limit:
                        break
                    res[find(i, j, k, n)] = res.get(find(i, j, k, n), 0) + 1
    print(sorted(res.items(), key=lambda x: (x[1], x[0])))
