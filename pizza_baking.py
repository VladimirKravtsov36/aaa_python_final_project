from random import randint
from pizza_recipes import Pizza


def log(message: str):
    """
    Декоратор - выводит рандоиное время и подставляет его в шаблон message
    """
    def log_decorator(func):

        def decorated(pizza: Pizza):
            rand_time = randint(1, 10)
            print(message.format(rand_time))

            return func(pizza)

        return decorated

    return log_decorator


@log('👨‍🍳 Приготовили за {}с!')
def bake(pizza: Pizza):
    """
    Готовит пиццу
    """
    pass


@log('🛵 Доставили за {}с!')
def home_delivery(pizza: Pizza):
    """
    Доставляет пиццу
    """
    pass


@log('🏠 Забарали за {}с!')
def pickup(pizza: Pizza):
    """
    Самовывоз
    """
    pass


if __name__ == '__main__':
    pass
