import os

from fabric.api import *
from tissu.api import *

def is_force_local():
    return current_hostdef().get("force_local", False)


def lrun(cmd):
    """
    local or remote run
    """
    if is_force_local():
        return local(cmd, capture=True)
    else:
        return run(cmd)    

def get_backupator_root():
    return current_hostdef().get("backupator_root", None)

def get_backup_dir():
    return current_hostdef().get("backup_dir", None)

@task
def backup():
    from backupator.conf import settings
    for process_task in getattr(settings,"BACKUP_PROCESS", []):
        execute("%s.backup" % (process_task,))