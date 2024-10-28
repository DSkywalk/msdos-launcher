# Copyright (C) 2019-2020  Patryk Obara <patryk.obara@gmail.com>
# Copyright (C) 2024  D_Skywalk
# SPDX-License-Identifier: GPL-2.0-or-later

"""
Useful functions and classes
"""

import hashlib
import os
import pathlib
import re
import zipfile


import os
import subprocess

from log import log

def wait_for_previous_process():
    """Wait for other process to end."""
    pid = 0
    try:
        with open('/tmp/msdos-launcher_wait.prc', 'r') as pid_file:
            pid = int(pid_file.read())
    except FileNotFoundError:
        pass
    if pid and os.path.isfile('/proc/{0}/cmdline'.format(pid)):
        log('waiting for process', pid, 'to stop and delete file', PID_FILE)
        subprocess.call(['inotifywait', '-e', 'delete', PID_FILE])


def sed(filename, regex_find, regex_replace):
    """Edit file in place."""
    with open(filename, 'r+') as txt:
        data = txt.read()
        txt.seek(0)
        txt.write(re.sub(regex_find, regex_replace, data))
        txt.truncate()


class PidFile:
    """Helper class to create and remove PID file"""

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        with open(self.file_name, 'w') as pid_file:
            pid_file.write(str(os.getpid()))
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass


def unzip(src_file, dst_dir):
    """Simply unzip a file."""
    archive = zipfile.ZipFile(src_file, 'r')
    archive.extractall(dst_dir)
    archive.close()


def sha256sum(path):
    """Simply compute sha256sum of a file."""
    algo = hashlib.sha256()
    with open(path, 'rb') as file:
        block = file.read()
        algo.update(block)
    return algo.hexdigest()


def get_lines(txt_file):
    """Simply get list of lines."""
    with open(txt_file) as tfile:
        return tfile.readlines()


# - SteamAppId - Steam sets this variable for games distributed through Steam
#
# - SteamGameId - Steam sets this variable for all games started via Steam
#                 interface. For non-Steam games this id is unique per
#                 game installation.
#
# - GOG_GAME_ID - Use this variable when starting GOG game whenever possible


def get_game_install_id():
    """Return a string identifying game installation"""
    steam_app_id = os.environ.get('SteamAppId', '0')
    gog_game_id = os.environ.get('GOG_GAME_ID', '0')
    steam_game_id = os.environ.get('SteamGameId', '0')
    if steam_app_id != '0':
        return steam_app_id
    if steam_game_id != '0':
        return steam_game_id
    if gog_game_id != '0':
        return gog_game_id
    return '0'


def get_game_global_id():
    """Return a string identifying specific game"""
    steam_app_id = os.environ.get('SteamAppId', '0')
    gog_game_id = os.environ.get('GOG_GAME_ID', '0')
    if steam_app_id != '0':
        return 'steam:' + steam_app_id
    if gog_game_id != '0':
        return 'gog:' + gog_game_id
    return None
