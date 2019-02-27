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
import re
import codecs

if __name__ == '__main__':
    # https://www.mathblog.dk/project-euler-89-develop-a-method-to-express-roman-numerals-in-minimal-form/
    with codecs.open('p089_roman.txt', 'r', encoding='utf-8') as fin:
        res = 0
        for line in fin:
            res += len(line) - len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", "  ", line))
        print(res)
