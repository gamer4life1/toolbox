#!/usr/bin/env python3


import click
import sys,os,git
from termcolor import colored, cprint

repo = git.Repo('.')
banner = """
########  #### ##    ##  ######     ###    ######## ####  ######    
##     ##  ##  ###   ## ##    ##   ## ##      ##    #### ##    ##   
##     ##  ##  ####  ## ##        ##   ##     ##     ##  ##         
########   ##  ## ## ## ##       ##     ##    ##    ##    ######    
##     ##  ##  ##  #### ##       #########    ##               ##   
##     ##  ##  ##   ### ##    ## ##     ##    ##         ##    ##   
########  #### ##    ##  ######  ##     ##    ##          ######    
########  #######   #######  ##       ########   #######  ##     ## 
   ##    ##     ## ##     ## ##       ##     ## ##     ##  ##   ##  
   ##    ##     ## ##     ## ##       ##     ## ##     ##   ## ##   
   ##    ##     ## ##     ## ##       ########  ##     ##    ###    
   ##    ##     ## ##     ## ##       ##     ## ##     ##   ## ##   
   ##    ##     ## ##     ## ##       ##     ## ##     ##  ##   ##  
   ##     #######   #######  ######## ########   #######  ##     ## 
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
    print(banner)

@cli.command()
def update():
    print(info('Updating submodules...'))
    for submodule in repo.submodules:
        print(info('Updating %s...' % (submodule.name)))
        submodule.update()
    print(good('Done!'))


#@click.command()
#def empire():

if __name__ == '__main__':
    cli()
