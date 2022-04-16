from time import time
from mpmath import mp

# Set decimal places to number of places - 1
mp.dps = 500000 - 1

print("Pi is approximately equal to:")

start_time = time()
print(mp.pi)
end_time = time()
seconds = end_time - start_time

print()
print("Done, {} digits in {} seconds".format(mp.dps+1, seconds))
