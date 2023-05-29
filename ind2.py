#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money():
    def __init__(self, a=0, b=1):
        a = int(a)
        b = int(b)

        if a < 0 or b < 0 or b > 99:
            raise ValueError()

        self.ruble = a
        self.penny = b

    def display(self):
        print(f"Cash: {self.ruble},{self.penny}₽")

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split('.', maxsplit=1)))

        if parts[0] < 0 or parts[1] < 0:
            raise ValueError()
        if len(str(parts[1])) == 1:
            parts[1] = int(str(parts[1]) + "0")

        self.ruble = int(parts[0])
        self.penny = int(parts[1])

    def add(self, rhs):
        if isinstance(rhs, Money):
            b = self.ruble * 100 + self.penny + rhs.ruble * 100 + rhs.penny
            a = b // 100
            b %= 100
            return Money(a, b)
        else:
            raise ValueError()

    def sub(self, rhs):
        if isinstance(rhs, Money):
            a = self.ruble - rhs.ruble
            b = self.penny - rhs.penny
            if b < 0:
                a -= 1
                b += 100
            return Money(a, b)
        else:
            raise ValueError()

    def mul(self, rhs):
        if isinstance(rhs, (int, float)):
            b = self.ruble * 100 + self.penny
            a = b * rhs
            a = int(a) // 100
            b = int(b) % 100
            return Money(a, b)
        else:
            raise ValueError()

    def div(self, rhs):
        if isinstance(rhs, Money):
            return self.div_money(rhs)
        elif isinstance(rhs, (int, float)):
            return self.div_number(rhs)
        else:
            raise ValueError()

    def div_money(self, rhs):
        if rhs.ruble == 0 and other.penny == 0:
            raise ValueError()
        a = self.ruble * 100 + self.penny
        b = rhs.ruble * 100 + rhs.penny
        return a / b

    def div_number(self, rhs):
        if rhs == 0:
            raise ValueError()
        a = self.ruble * 100 + self.penny
        a /= rhs
        a = round(a, 2)
        b = int(a // 100)
        a %= 100
        return Money(b, a)

    def equals(self, rhs):
        if isinstance(rhs, Money):
            return (self.ruble == rhs.ruble) and \
            (self.penny == rhs.penny)
        else:
            return False

    def greater(self, rhs):
        if isinstance(rhs, Money):
            v1 = (self.ruble + self.penny) / 100
            v2 = (rhs.ruble + rhs.penny) / 100
            return v1 > v2
        else:
            return False

    def less(self, rhs):
        if isinstance(rhs, Money):
            v1 = (self.ruble + self.penny) / 100
            v2 = (rhs.ruble + rhs.penny) / 100
            return v1 < v2
        else:
            return False


if __name__ == '__main__':
    cp = Money()
    cp.read("Введите денежную сумму: ")
    cp.display()

    cp1 = Money(3, 40)
    cp1.display()

    cp2 = cp1.add(cp)
    cp2.display()

    cp3 = cp.sub(cp1)
    cp3.display()

    cp4 = cp.div(33.3)
    cp4.display()

    cp5 = cp.mul(4)
    cp5.display()

    print(cp.less(cp1))
