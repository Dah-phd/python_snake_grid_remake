import subprocess
from sys import platform

if __name__ == '__main__':
    input('Press ENTER to start new game!')
    if platform[:3] == 'win':
        cmd = 'res\\GUI.pyw'
    else:
        cmd = 'python3 ./res/GUI.pyw'
    subprocess.Popen(cmd, stdin=None, stdout=None, stderr=None, shell=True,
                     close_fds=True, creationflags=subprocess.DETACHED_PROCESS)
