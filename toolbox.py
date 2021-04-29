#!/usr/bin/env python3


import click
import sys,os,git
from termcolor import colored, cprint
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


repo = git.Repo('/opt/toolbox')


banner1 = """
████████  ████ ██    ██
██     ██  ██  ███   ██
██     ██  ██  ████  ██
████████   ██  ██ ██ ██
██     ██  ██  ██  ████
██     ██  ██  ██   ███
████████  ████ ██    ██
"""


banner2 = """
 ██████     ███    ████████ ████  ██████
██    ██   ██ ██      ██    ████ ██    ██
██        ██   ██     ██     ██  ██
██       ██     ██    ██    ██    ██████
██       █████████    ██               ██
██       █████████    ██               ██
 ██████  ██     ██    ██          ██████
"""

banner3 = """
████████  ███████   ███████  ██
   ██    ██     ██ ██     ██ ██
   ██    ██     ██ ██     ██ ██
   ██    ██     ██ ██     ██ ██
   ██    ██     ██ ██     ██ ██
   ██    ██     ██ ██     ██ ██
   ██     ███████   ███████  ████████
"""

banner4 = """
████████   ███████  ██     ██
██     ██ ██     ██  ██   ██
██     ██ ██     ██   ██ ██
████████  ██     ██    ███
██     ██ ██     ██   ██ ██
██     ██ ██     ██  ██   ██
████████   ███████  ██     ██
"""


def good(text):
    ctext = colored('[+] ' + text, 'green')
    return ctext

def info(text):
    ctext = colored('[-] ' + text, 'white')
    return ctext

def error(text):
    ctext = colored('[!] ' + text, 'red')
    return ctext

@click.group()
def cli():
    print(colored(banner1.rstrip(), 'blue'), end=' ')
    print(colored(banner2.rstrip(), 'red'), end=' ')
    print(colored(banner3.rstrip(), 'blue'), end=' ')
    print(colored(banner4.rstrip(), 'red'), end=' ')

@cli.command()
def setuptools():
    if os.getuid() != 0:
        print(error("You need to run the setup command as root!"))
        exit(1)
    print(info("Setting up Empire..."))
    installempire = subprocess.run(['bash', '/opt/toolbox/tools/Empire/setup/install.sh'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(installempire)
#    if installempire.poll() != 0:
#        print(error("Failed to install Empire!"))
#        exit(1)
#    print(good("Installed Empire!"))
#    print(info("Installing search-that-hash, name-that-hash & ciphey..."))
#    install("search-that-hash")
#    install("name-that-hash")
#    install("ciphey")
#    print(good("Done!"))

@cli.command()
def updatetools():
    print(info('Updating submodules...'))
    for submodule in repo.submodules:
        print(info('Updating %s...' % (submodule.name)))
        submodule.update()
    print(good('Done!'))


#@click.command()
#def empire():


if __name__ == '__main__':
    cli()
