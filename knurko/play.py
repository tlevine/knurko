import subprocess as sp

def play(filename):
    mplayer = sp.Popen(['mplayer', filename],
                    stdout = sp.PIPE, stderr = sp.PIPE)
    stdout, stderr = mplayer.communicate()
    stdout.decode('utf-8').split('\r')[-2]
