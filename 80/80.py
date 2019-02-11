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
from decimal import *
from utils import is_square


if __name__ == '__main__':
    getcontext().prec = 105
    res = 0
    for i in range(1, 101):
        if is_square(i):
            continue
        tem = str(Decimal(i).sqrt())
        res += sum([int(x) for x in tem[:101] if x != '.'])
    print(res)
