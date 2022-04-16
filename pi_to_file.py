import sys
from time import time
from mpmath import mp

# Set decimal places to number of places - 1
mp.dps = 500000 - 1
f = open("pi.txt", "w")

start_time = time()
f.write(str(mp.pi))
end_time = time()
seconds = end_time - start_time

f.close()

print("Done, {} digits in {} seconds".format(mp.dps+1, seconds))
