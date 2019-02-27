"hér verður borð 2 kóðað"
import random


i=1
k={}
m=0

j=random.randint(1,4)

print("Þú hefur valið töluna 1")

if j==2:
    k=3,4
    m=2
    print("Kistur", k,"er opnar og þær eru tómar")
else:
    k=2
    print("Kista", k,"er opnar og þær eru tómar")
    if j==3:
        k=4
        m=3
        print("Kista", k,"er opnar og þær eru tómar")
    else:
        k=3
        m=4
    print("Kista", k,"er opnar og þær eru tómar")
c = int(input("Viltu breyta um val (1=breyta, 0=ekki breyta); "))
if c==0:
    print("Leikmaður breyti ekki, hann er með kistu", i)
else:
    print ("Leikur skipti yfir í kistu", m)
    i=m
if i==j:
    print ("Til hamingju þú vanst!")
else:
    print("Því miður vanstu ekki.")
