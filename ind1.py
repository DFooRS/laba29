#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int) or b < 0 or a < 0:
            raise ValueError()

        self.__first = a
        self.__second = b

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split('.', maxsplit=1)))

        if parts[1] < 0 or parts[0] < 0:
            raise ValueError()

        self.__first = parts[0]
        self.__second = parts[1]

    def multiply(self, number):
        if isinstance(number, int):
            result = (self.first * 100 + self.second) * number
            return Pair(result // 100, result % 100)
        else:
            raise ValueError()

    def display(self):
        print(f"first: {self.__first}, second: {self.__second}")


def make_pair(a, b):
    try:
        return Pair(a, b)
    except:
        ValueError()


if __name__ == '__main__':
    pair = make_pair(1, 90)
    pair.display()
    number = int(input("Введите целое число: "))
    result = pair.multiply(number)
    result.display()
