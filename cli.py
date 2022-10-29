import click
from pizza_recipes import Pepperoni, Margherita, Hawaiian
from pizza_baking import bake, home_delivery, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """
    Готовит и доставляет пиццу
    """
    if pizza.lower() == 'margherita':
        pizza_object = Margherita()
    elif pizza.lower() == 'pepperoni':
        pizza_object = Pepperoni()
    elif pizza.lower() == 'hawaiian':
        pizza_object = Hawaiian()
    else:
        click.echo('Такой пиццы нет :(')
        return

    click.echo(bake(pizza_object), nl=False)

    if delivery:
        click.echo(home_delivery(pizza_object), nl=False)
    else:
        click.echo(pickup(pizza_object), nl=False)


@cli.command()
def menu():
    """
    Выводит меню
    """
    click.echo(Pepperoni())
    click.echo(Margherita())
    click.echo(Hawaiian())


if __name__ == '__main__':
    cli()
