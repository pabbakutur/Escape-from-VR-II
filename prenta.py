import sys
import time

string = 'hello world\n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.25)
