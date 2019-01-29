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


def calc_reminder_loop_size(x, y):
    reminders = []
    while True:
        reminder = x * 10 % y
        if reminder == 0:
            return 0
        if reminder in reminders:
            return len(reminders) - reminders.index(reminder)
        reminders.append(reminder)
        x = reminder


if __name__ == '__main__':
    res = 0
    max_len = 0
    # print(calc_reminder_loop_size(1, 7))
    for i in range(2, 1000):
        loop_size = calc_reminder_loop_size(1, i)
        if max_len < loop_size:
            max_len = loop_size
            res = i

    print(res)
