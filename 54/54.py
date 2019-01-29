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
from enum import Enum


class CombinationType(Enum):
    HighCard = 0
    OnePair = 1
    TwoPairs = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8
    RoyalFlush = 9


class Combination(object):
    def __init__(self, cards):
        self.cards = cards
        self.sorted_cards = sorted(self.cards)
        self.sorted_values = [card.value for card in self.sorted_cards]
        self.sorted_units = [card.unit for card in self.sorted_cards]
        self.combination_type = self.get_type()

    def __repr__(self):
        return str(self.sorted_cards)

    def get_type(self):
        if self.is_royal_flush():
            return CombinationType.RoyalFlush
        if self.is_straight_flush():
            return CombinationType.StraightFlush
        if self.is_four_of_a_kind():
            return CombinationType.FourOfAKind
        if self.is_full_house():
            return CombinationType.FullHouse
        if self.is_flush():
            return CombinationType.Flush
        if self.is_straight():
            return CombinationType.Straight
        if self.is_three_of_a_kind():
            return CombinationType.ThreeOfAKind
        if self.is_two_pairs():
            return CombinationType.TwoPairs
        if self.is_one_pair():
            return CombinationType.OnePair
        return CombinationType.HighCard

    def is_royal_flush(self):
        return len(set(self.sorted_values)) == 5 and self.sorted_values[0] == 10 \
               and self.sorted_values[-1] == 14 and len(set(self.sorted_units)) == 1

    def is_straight_flush(self):
        return len(set(self.sorted_values)) == 5 and self.sorted_values[-1] - self.sorted_values[0] == 4 \
               and len(set(self.sorted_units)) == 1

    def is_four_of_a_kind(self):
        return len(set(self.sorted_values)) == 2 and (self.sorted_values.count(self.sorted_values[0]) == 1
                                                      or self.sorted_values.count(self.sorted_values[0]) == 4)

    def is_full_house(self):
        return len(set(self.sorted_values)) == 2 and (self.sorted_values.count(self.sorted_values[0]) == 2
                                                      or self.sorted_values.count(self.sorted_values[0]) == 3)

    def is_flush(self):
        return len(set(self.sorted_units)) == 1

    def is_straight(self):
        return len(set(self.sorted_values)) == 5 and self.sorted_values[-1] - self.sorted_values[0] == 4

    def is_three_of_a_kind(self):
        return self.sorted_values.count(self.sorted_values[0]) == 3 \
               or self.sorted_values.count(self.sorted_values[1]) == 3 \
               or self.sorted_values.count(self.sorted_values[2]) == 3 \
               or self.sorted_values.count(self.sorted_values[3]) == 3

    def is_two_pairs(self):
        return len(set(self.sorted_values)) == 3

    def is_one_pair(self):
        return len(set(self.sorted_values)) == 4

    def is_high_card(self):
        return len(set(self.sorted_values)) == 5

    def get_the_four_times_card(self):
        return self.sorted_values[2]

    def get_the_three_times_card(self):
        return self.sorted_values[2]

    def get_the_two_pair_card(self):
        res = []
        for value in set(self.sorted_values):
            if self.sorted_values.count(value) == 2:
                res.append(value)
        return sorted(set(res))

    def get_the_single_card(self):
        for value in self.sorted_values:
            if self.sorted_values.count(value) == 1:
                return value

    def get_the_one_pair(self):
        for value in self.sorted_values:
            if self.sorted_values.count(value) == 2:
                return value

    def get_the_reminder_three_single_card(self):
        res = []
        for value in self.sorted_values:
            if self.sorted_values.count(value) == 1:
                res.append(value)
        return res

    @staticmethod
    def compare_single_cards(a, b):
        assert len(a) == len(b)
        for i in range(len(a) - 1, -1, -1):
            if a[i] != b[i]:
                return a[i] > b[i]

    def __gt__(self, other):
        if self.combination_type.value > other.combination_type.value:
            return True
        if self.combination_type.value < other.combination_type.value:
            return False
        if self.combination_type == CombinationType.StraightFlush:
            return self.sorted_values[0] > other.sorted_values[0]
        if self.combination_type == CombinationType.FourOfAKind:
            return self.get_the_four_times_card() > other.get_the_four_times_card()
        if self.combination_type == CombinationType.FullHouse:
            return self.get_the_three_times_card() > other.get_the_three_times_card()
        if self.combination_type == CombinationType.Flush:
            return self.sorted_values[-1] > other.sorted_values[-1]
        if self.combination_type == CombinationType.Straight:
            return self.sorted_values[-1] > other.sorted_values[-1]
        if self.combination_type == CombinationType.ThreeOfAKind:
            return self.get_the_three_times_card() > other.get_the_three_times_card()
        if self.combination_type == CombinationType.TwoPairs:
            a, b = self.get_the_two_pair_card()
            oa, ob = self.get_the_two_pair_card()
            if a == oa and b == ob:
                return self.get_the_single_card() > other.get_the_single_card()
            if b == ob:
                return a > oa
            return b > ob
        if self.combination_type == CombinationType.OnePair:
            a = self.get_the_one_pair()
            oa = other.get_the_one_pair()
            if a == oa:
                b = self.get_the_reminder_three_single_card()
                ob = self.get_the_reminder_three_single_card()
                return self.compare_single_cards(b, ob)
            return a > oa
        return self.compare_single_cards(self.sorted_values, other.sorted_values)


class Card(object):
    def __init__(self, value, unit):
        self.value = self.get_value(value)
        self.unit = unit

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return str(self.value) + ' ' + str(self.unit)

    @staticmethod
    def get_value(x):
        if x == 'T':
            return 10
        if x == 'J':
            return 11
        if x == 'Q':
            return 12
        if x == 'K':
            return 13
        if x == 'A':
            return 14
        return int(x)


if __name__ == '__main__':
    # a = Combination([Card('3', 'D'), Card('7', 'H'), Card('T', 'S'), Card('K', 'S'), Card('A', 'D')])
    # b = Combination([Card('2', 'D'), Card('J', 'H'), Card('J', 'S'), Card('Q', 'D'), Card('A', 'C')])
    # if a > b:
    #     pass
    with codecs.open('p054_poker.txt', 'r', encoding='utf-8') as fin:
        res = 0
        for line in fin:
            line = line.strip().split()
            a = Combination([Card(x[0], x[1]) for x in line[:5]])
            b = Combination([Card(x[0], x[1]) for x in line[5:]])
            if a > b:
                print(a, b)
                res += 1
        print(res)
