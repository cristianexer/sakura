import click
from sanic.cli import AppGroup

commands = AppGroup('commands')


@commands.command("say")
@click.argument("something")
def say_something(something):
    print(something)