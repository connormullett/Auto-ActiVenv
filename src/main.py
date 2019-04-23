
import os, sys
import click


@click.command()
@click.argument('path')
def install(path):
    '''
    install autovenv script\n
    PATH = path to login shell\n
    use the command `which $SHELL`\n
    or do `activenv $(which $SHELL)`\n
    to determine your shell and\n
    the path to it
    '''
    click.echo(path)

