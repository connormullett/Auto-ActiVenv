
import os, sys, subprocess
import click
from .script import Script


@click.command()
@click.option('-p', '--path', help='path to shell')
@click.option('-s', '--shell', help='the name of the shell')
@click.option('--no-backup', is_flag=True)
def install(path, shell, no_backup):
    if not path:
        path = subprocess.getoutput('which $SHELL')

    if not shell:
        shell = path.split('/')[-1]

    home = os.getenv('HOME')

    if not no_backup:
        os.system('cp %s/.%src %s/.%src_backup' % (home, shell, home, shell))

    if not os.path.exists(os.path.join(home, '.%src' % (shell))):
        click.echo('No RC file found :: exiting')
        sys.exit(1)
    with open('%s/.%src' % (home, shell), 'a+') as f:
        if not Script in f.read():
            f.write(Script)
            click.echo('already installed :: exiting')
            sys.exit(0)
    click.secho('DONE', fg='cyan', bold=True)

