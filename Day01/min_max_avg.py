# Program to extract the minimum, maximum and
# Average of the user given numbers

# Input
L = []
ud = ''
while ud != 'q':
    ud = input('## (q to quit) ? ')
    if(ud.isdigit()):
        L.append(int(ud))

print('-'*60)
print('VALID INPUTS:')
print(L)
print('-'*60)

# Process

minimum = min(L)
maximum = max(L)
average = sum(L)/len(L)

# Output
print('MINIMUM : ', minimum)
print('MAXIMUM : ', maximum)
print('AVERAGE : ', average)
