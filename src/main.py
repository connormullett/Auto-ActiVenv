
import os, sys
import click
from .script import create_script
import platform

if int(platform.python_version_tuple()[0]) < 3:
    version = 2
    import commands
else:
    version = 3
    import subprocess


@click.command()
@click.option('-p', '--path', help='path to shell')
@click.option('-s', '--shell', help='the name of the shell')
@click.option('--no-backup', help='choose to not make a backup of conf file', is_flag=True)
@click.option('-n', '--name', help='the common name of your virtual environments, if you tend to name your virt environments differently, use --not-common', default='venv')
@click.option('--no-common', is_flag=True, help='NOT IMPLEMENTED')
def install(path, shell, no_backup, name):

    install_script = create_script(name)

    if not path:
        if version == 3:
            path = subprocess.getoutput('which $SHELL')
        else:
            path = commands.getoutput('which $SHELL')

    if not shell:
        shell = path.split('/')[-1]

    home = os.getenv('HOME')

    if not no_backup:
        os.system('cp %s/.%src %s/.%src_backup' % (home, shell, home, shell))

    if not os.path.exists(os.path.join(home, '.%src' % (shell))):
        click.echo('No RC file found :: exiting')
        sys.exit(1)
    with open('%s/.%src' % (home, shell), 'a+') as f:
        f.write(install_script)
    click.secho('DONE', fg='cyan', bold=True)

