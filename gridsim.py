# Simulates the grid

import sys
from time import sleep

# Dummy
class Pattern:
    tracking = 0

from pattern_one import *

time = 0.0
pattern = PatternSpin()
delay = 0

while (1):
    print "Time is %d seconds"%(time)

    time += delay

    lights, delay = pattern.update()

    for x in range(7):
        for y in range(7):
            if lights[x][y]:
                sys.stdout.write('# ')
            else:
                sys.stdout.write('  ')
        print

    for i in range(8):
        sys.stdout.write("\033[F") # Cursor up one line

    sleep(delay)
