from datetime import datetime

t1 = datetime.now()

for i in range(300):
    print('-',end='')

t2 = datetime.now()

print('Time elapsed: ', t2 - t1)
