import myprime
import random

rn = []
for i in range(100):
    rn.append(random.randint(1, 100))

primes = []
for n in rn:
    if(myprime.checkprime(n)):
        primes.append(n)

print(primes)
    
