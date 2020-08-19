from dataclasses import dataclass
from functools import total_ordering


@dataclass
@total_ordering
class Card:
    value: int
    suit: str
    owner: str

    __CONV_MAP = {
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A'
    }

    def __str__(self) -> str:
        return f'{self.__CONV_MAP[self.value]} of {self.suit} ({self.owner}\'s)'

    def __repr__(self) -> str:
        return f'Card({self.__CONV_MAP[self.value]}, {self.suit}, {self.owner}\'s)'

    def __is_valid_operand(self, other) -> bool:
        return hasattr(other, 'value')

    def __eq__(self, other) -> bool:
        if not self.__is_valid_operand(other):
            return NotImplemented
        return self.value == other.value

    def __gt__(self, other) -> bool:
        if not self.__is_valid_operand(other):
            return NotImplemented
        return self.value > other.value
