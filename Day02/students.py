# Read the file and build the data structure for processing

file = r"C:\Users\Purushotham\Desktop\Clients\IBM\Day02\students.csv"
f = open(file, "r")

D = {}
cols = f.readline().strip().split(',')
data = f.readline()

while data != '':
    print(data)
    d = dict(zip(cols, data.strip().split(',')))
    D.update({d['regid']: d})
    data = f.readline()

f.close()



# Calculate the averages

for rec  in D.values():
    rec['avg'] = (float(rec['phy']) + float(rec['math']) + float(rec['chem']) + float(rec['bio'])) / 4
'''
for key  in D.keys():
    D[key]['avg'] = (float(D[key]['phy']) + float(D[key]['math']) + float(D[key]['chem']) + float(D[key]['bio'])) / 4
'''

# Calculate the rank

avgs = []
for rec in D.values():
    avgs.append(rec['avg'])
avgs = set(avgs)
avgs = sorted(list(avgs), reverse=True)

rank = 1
for avg in avgs:
    for rec in D.values():
        if(rec['avg'] == avg):
            rec['rank'] = rank
    rank += 1

    
# Print the report
    
print(D)
