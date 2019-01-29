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
import codecs


if __name__ == '__main__':
    with codecs.open('name.txt', 'r', encoding='utf-8') as fin:
        line = [x.replace("\"", "") for x in fin.read().split(',')]
        line = sorted(line)
        res = 0
        for idx, name in enumerate(line):
            res += sum([ord(x) - ord('A') + 1 for x in name]) * (idx + 1)
        print(res)
