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


def is_leap_year(year):
    return year & 3 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == '__main__':
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    res = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            days = month_days[month]
            if month == 2:
                days += 1 if is_leap_year(year) else 0
            total_days += days
            next_month_begin = total_days % 7 + 1
            if year > 1900 and not (year == 2000 and month == 12):
                res += 1 if next_month_begin == 7 else 0
    print(res)
