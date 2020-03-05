class emp(object):

    # Data/variables
    def __init__(self, n, a):
        self.name = n
        self.age  = a
        self.addr = ''
        self.salary = ''
        self.income = ''
        self.tax = ''


    # Functions/methods

    def setname(self, n):
        self.name = n

    def setage(self, a):
        self.age = a

    def getname(self):
        return self.name

    def getage(self):
        return self.age


    def printinfo(self):
        print(self.name, self.age)

##################################################################

e1 = emp('Anil', 30)
e2 = emp('Sunil', 30)

e1.printinfo()
e2.printinfo()

e1.setname('Webstar')
e1.setage(40)

e1.printinfo()
e2.printinfo()

s = {e1, e2}
print(s)
    
