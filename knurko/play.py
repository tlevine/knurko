#!/usr/bin/env python3
import subprocess as sp

bill = sp.Popen(['mplayer', '/home/tlevine/Bill Nye the Science Guy/Water Cycle.avi'], stdout = sp.PIPE, stderr = sp.PIPE)
stdout, stderr = bill.communicate()
stdout
stderr
stdout
stdout.split('\n')
stdout.decode('utf-8')
stdout.decode('utf-8').split('\n')
stdout.decode('utf-8').split('\r')
stdout.decode('utf-8').split('\r')[-2]
stdout.decode('utf-8').split('\r')[-2]
history

