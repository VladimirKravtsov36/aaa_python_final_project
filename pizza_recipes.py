from typing import Dict


class Pizza:

    def __init__(self, size: str = 'L'):

        if size not in ['L', 'XL']:
            raise ValueError('Invalid size, avalaible sizes: L, XL')

        self.size = size
        self.emoji = ''
        self.ingridients = []

    def dict(self) -> Dict:

        return {'recipe': self.ingridients}

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Pizza):
            return NotImplemented

        return sorted(self.ingridients) == sorted(other.ingridients) and \
            self.size == other.size

    def __str__(self) -> str:
        return (f'{self.__class__.__name__} {self.emoji}: '
                f'{(", ").join(self.ingridients)}')


class Margherita(Pizza):

    def __init__(self, size: str = 'L'):
        super().__init__(size)
        self.emoji = '🧀'
        self.ingridients = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):

    def __init__(self, size: str = 'L'):
        super().__init__(size)
        self.emoji = '🍕'
        self.ingridients = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):

    def __init__(self, size: str = 'L'):
        super().__init__(size)
        self.emoji = '🍍'
        self.ingridients = ['tomato sauce', 'mozzarella', 'chicken',
                            'pineapples']


if __name__ == '__main__':
    pass
