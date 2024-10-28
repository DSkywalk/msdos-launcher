# Copyright (C) 2019-2020  Patryk Obara <patryk.obara@gmail.com>
# Copyright (C) 2024  D_Skywalk
# SPDX-License-Identifier: GPL-2.0-or-later

"""
Log functions
"""

import sys

PREFIX = 'DOS:'


def print_err(*value, sep=' ', end='\n', flush=False):
    """Prints the values to stderr."""
    print(*value, sep=sep, end=end, file=sys.stderr, flush=flush)


def log(*value, sep=' ', end='\n', flush=False):
    """Prints the values to stderr with prefix."""
    print_err(PREFIX, *value, sep=sep, end=end, flush=flush)


def log_err(*value, sep=' ', end='\n', flush=False):
    """Prints the values to stderr with prefix and 'error:'"""
    log('error:', *value, sep=sep, end=end, flush=flush)


def log_warn(*value, sep=' ', end='\n', flush=False):
    """Prints the values to stderr with prefix and 'warning:'"""
    log('warning:', *value, sep=sep, end=end, flush=flush)



def zenity_err(msg: str) -> None:
    steam_zenity = os.environ.get('STEAM_ZENITY', '/usr/bin/zenity')
    cmd = [steam_zenity, '--error', '--no-wrap', '--title=Boxtron Error']
    log_err(msg)
    if os.path.isfile(steam_zenity):
        subprocess.call(cmd + ['--text={}'.format(msg)])
    else:
        log_err('zenity ({}) is missing'.format(steam_zenity))


def zenity_info(msg: str) -> None:
    steam_zenity = os.environ.get('STEAM_ZENITY', '/usr/bin/zenity')
    cmd = [steam_zenity, '--info', '--no-wrap', '--title=Boxtron Error']
    log(msg)
    if os.path.isfile(steam_zenity):
        subprocess.call(cmd + ['--text={}'.format(msg)])
    else:
        log_err('zenity ({}) is missing'.format(steam_zenity))

