# Generate random numbers
import random
rn = []
for i in range(100):
    rn.append(random.randint(1, 100))

print('\nRANDOMS:')
print(rn)

# Separate odds and evens

odds = []
evens = []
for n in rn:
    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

print('\nODDS:')
print(odds)
print('\nEVENS:')
print(evens)
