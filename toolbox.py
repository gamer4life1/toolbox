#!/usr/bin/env python3


import click
import sys,os,git
from termcolor import colored, cprint

repo = git.Repo('.')

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
    pass


def update():
    print(info('Updating submodules...'))
    for submodule in repo.submodules:
        print(green('Updating %s...' % (submodule.name)))
        submodule.update(init=True)


@click.command()
def empire():
    
