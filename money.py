"""Class for calculate different money."""

import json
import requests


class Money(object):
    """Class for calculate different money."""

    def __init__(self, value, curr='USD'):
        """Initialize money(value and currency)."""
        self.value = value
        self.curr = curr
        self.url = ("http://free.currencyconverterapi.com/api/v6/convert?"
                    "q={source}_{dest}&compact=y&apiKey=495edc98a0726481ef3c")

    def __add__(self, other_money):
        """Magic method for calculate with other money."""
        res = requests.get(url=self.url.format(source=other_money.curr,
                                               dest=self.curr))
        exchange = json.loads(res.text).get('{}_{}'.format(other_money.curr,
                                                           self.curr))
        return Money(self.value + other_money.value * exchange.get('val'),
                     self.curr)

    def __radd__(self, other_money):
        """Magic method for sum with other money."""
        if isinstance(other_money, int):
            return self
        else:
            super(self.__add__(other_money))

    def __repr__(self):
        """Magic method for beautiful output money."""
        return '{} {}'.format(round(self.value, 2), self.curr)


if __name__ == '__main__':
    m = Money(10, 'USD')
    m2 = Money(10, 'BYN')
    m3 = Money(100, 'BYN')
    lst = [m, m2, m3]
    print(sum(lst))
