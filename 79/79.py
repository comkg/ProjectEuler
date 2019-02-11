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
    def judge(x):
        guess = '73162890'
        start = 0
        for c in x:
            start = guess.find(c, start)
            if start == -1:
                return False
        return True

    with codecs.open('p079_keylog.txt') as fin:
        for line in fin:
            if not judge(line.strip()):
                print(line.strip())
