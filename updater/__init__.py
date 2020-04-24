'''Module that does updating related tasks'''
import os
import sys
import time
import threading
import subprocess


def is_out_of_date(cwd):
    ''' Checks if the git version is out of date '''
    local = subprocess.check_output('git fetch', cwd=cwd, timeout=30)
    local = subprocess.check_output('git rev-parse HEAD', cwd=cwd, timeout=30)
    remote = subprocess.check_output('git rev-parse @{u}', cwd=cwd, timeout=30)
    if local != remote:
        return True
    return False


def update_task(logger, update_interval):
    '''Periodically updates the bot'''
    while True:
        update(logger)
        time.sleep(update_interval)


def start_update_task(logger, update_interval):
    '''Periodically updates the bot in a thread'''
    threading.Thread(target=update_task, args=[logger, update_interval], daemon=True).start()


def wait_for_update(logger=None, update_interval=60):
    '''Periodically updates the bot in a thread'''
    if logger is not None:
        logger.log('Waiting for a update...')
    while True:
        update()
        time.sleep(update_interval)


def update(logger=None):
    '''Checks for updates and updates if out of date'''
    if logger is not None:
        logger.log('Checking for updates...')
    try:
        updated = False
        if is_out_of_date(None):
            if logger is not None:
                logger.log('Updating...')
            output = subprocess.check_output('git name-rev --name-only HEAD', timeout=30)
            branch = output.decode('utf-8').rstrip()
            subprocess.run('git fetch', check=True, timeout=30)
            subprocess.run(f'git reset --hard origin/{branch}', check=True, timeout=30)
            updated = True
        if updated:
            if logger is not None:
                logger.log('Successfully updated. Now, restarting.')
            time.sleep(5)
            os.execl(sys.executable, sys.executable, *sys.argv)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        if logger is not None:
            logger.log('Updating failed.')
