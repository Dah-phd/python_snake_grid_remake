import subprocess
from sys import platform
if platform == 'linux':
    from os import setpgrp

if __name__ == '__main__':
    input('Press ENTER to start new game!')
    if platform[:3] == 'win':
        subprocess.Popen('res\\GUI.pyw', stdin=None, stdout=None, stderr=None, shell=True,
                         close_fds=True, creationflags=subprocess.DETACHED_PROCESS)
    else:
        subprocess.Popen('python3 ./res/GUI.pyw', stdin=None, stdout=None, stderr=None, shell=True,
                         close_fds=True, preexec_fn=setpgrp)
