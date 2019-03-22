import sys
import time

string = "Lexi situr á lesstofunni að leggja lokahönd á heimavinnuna sína.\nHann hefur aldrei verið sterkur að heilda eða diffra, þú þarft að hjálpa honum.\nÞú færð 3 tilraunir til að svara 2 spurningum réttum.\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)


##################

string = "Lexi situr á lesstofunni að leggja lokahönd á heimavinnuna sína.\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)

string = "Hann hefur aldrei verið sterkur að heilda eða diffra, þú þarft að hjálpa honum.\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)

string = "Þú færð 3 tilraunir til að svara 2 spurningum réttum.\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)
