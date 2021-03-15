import subprocess
import scoring
from sys import argv, platform


def scores(val):
    link = scoring.highscore(
        'res\\db.res' if platform[:3] == 'win' else './res/db.res')
    print('GAME OVER')
    val = int(val)
    if val > 0:
        print(f'Your socre is {val}')
        link.name = input('ENTER NAME: ')
        link.new_score(val)
    hs = link.quarry()
    if hs:
        if len(hs) > 20:
            hs = hs[:20]
        for n, score in enumerate(hs):
            print(f'{n+1} position: {score[0]} with {score[1]} points')


if __name__ == '__main__':
    scores(argv[1])
    dat = input('Press ENTER for new game or Q to exit!')
    if dat != 'q':
        print(platform[:3])
        if platform[:3] == 'win':
            subprocess.Popen('res\\GUI.pyw', shell=True, creationflags=subprocess.DETACHED_PROCESS,
                             stderr=None, stdin=None, stdout=None, close_fds=True)
        else:
            subprocess.Popen('python3 ./res/GUI.pyw', shell=True, creationflags=subprocess.DETACHED_PROCESS,
                             stderr=None, stdin=None, stdout=None, close_fds=True)
