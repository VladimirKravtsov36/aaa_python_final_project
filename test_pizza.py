from typing import List, Dict
import re
import pytest
from click.testing import CliRunner
from cli import order, menu
from pizza_recipes import Pizza, Hawaiian, Pepperoni, Margherita


@pytest.mark.parametrize(
    'pizza, result',
    [
        (Pepperoni, 'Pepperoni 🍕: tomato sauce, mozzarella, pepperoni'),
        (Margherita, 'Margherita 🧀: tomato sauce, mozzarella, tomatoes'),
        (Hawaiian, 'Hawaiian 🍍: tomato sauce, mozzarella, chicken, ' +
                   'pineapples'),
    ],
    )
def test_pizza_str(pizza: Pizza, result):
    """
    Проверяет корректность представления пиццы в виду строки
    """
    assert str(pizza()) == result


@pytest.mark.parametrize(
    'pizza, result',
    [
        (Pepperoni, {'recipe': ['tomato sauce', 'mozzarella', 'pepperoni']}),
        (Margherita, {'recipe': ['tomato sauce', 'mozzarella', 'tomatoes']}),
        (Hawaiian, {'recipe': ['tomato sauce', 'mozzarella', 'chicken',
                               'pineapples']}),
    ],
    )
def test_pizza_dict(pizza: Pizza, result: Dict):
    """
    Проверка метода dict()
    """
    assert pizza().dict() == result


def test_pizza_eq():
    """
    Проверка оператора сравнения
    """
    assert Margherita() == Margherita()
    assert Margherita('L') != Margherita('XL')
    assert Pepperoni('L') != Hawaiian('L')


def test_wrong_size():
    """
    Проверка размера пиццы
    """
    with pytest.raises(ValueError):
        Pepperoni('XXL')


def test_cli_menu():
    """
    Проверка cli команды menu
    """
    runner = CliRunner()
    result = runner.invoke(menu)
    out = result.output

    assert out == ('Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n'
                   'Margherita 🧀: tomato sauce, mozzarella, tomatoes\n'
                   'Hawaiian 🍍: tomato sauce, mozzarella, chicken, '
                   'pineapples\n')


@pytest.mark.parametrize(
    'arguments, result',
    [
        (['pepperoni'], ('👨‍🍳 Приготовили за {}с!\n'
                         '🏠 Забарали за {}с!\n')),
        (['margherita'], ('👨‍🍳 Приготовили за {}с!\n'
                          '🏠 Забарали за {}с!\n')),
        (['hawaiian', '--delivery'], ('👨‍🍳 Приготовили за {}с!\n'
                                      '🛵 Доставили за {}с!\n')),
        (['some pizza'], 'Такой пиццы нет :(\n'),
    ],
)
def test_cli_order(arguments: List[str], result: str):
    """
    Проверка cli команды order
    """
    runner = CliRunner()
    out = runner.invoke(order, arguments).output
    print(out)
    out = re.sub(r'\d+', '{}', out)

    assert out == result


if __name__ == '__main__':
    pass
