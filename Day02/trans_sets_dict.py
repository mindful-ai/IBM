Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Sets
>>> s1 = set('abcdefg')
>>> s1
{'e', 'd', 'f', 'a', 'g', 'b', 'c'}
>>> s2 = { 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> s2
{'e', 'i', 'd', 'j', 'g', 'f', 'h'}
>>> s1 & s2
{'f', 'e', 'd', 'g'}
>>> s1 | s2
{'e', 'i', 'd', 'f', 'j', 'a', 'g', 'b', 'c', 'h'}
>>> s1 ^ s2
{'i', 'j', 'a', 'b', 'c', 'h'}
>>> s1
{'e', 'd', 'f', 'a', 'g', 'b', 'c'}
>>> s1.add('x')
>>> s1
{'e', 'd', 'f', 'x', 'a', 'g', 'b', 'c'}
>>> s3 = {'y', 'z'}
>>> s2.update(s3)
>>> s2
{'e', 'y', 'i', 'd', 'j', 'z', 'g', 'f', 'h'}
>>> L = ['red', 'green']
>>> s3.update(L)
>>> s3
{'y', 'red', 'green', 'z'}
>>> L
['red', 'green']
>>> L.extend(s2)
>>> L
['red', 'green', 'e', 'y', 'i', 'd', 'j', 'z', 'g', 'f', 'h']
>>> s3.update({'name':'anil', 'age':35})
>>> s3
{'y', 'green', 'age', 'name', 'red', 'z'}
>>> d = {'name':'anil', 'age':35}
>>> for item in d:
	print(item)

	
name
age
>>> s3.update(d.items())
>>> s3
{'y', 'green', ('name', 'anil'), 'age', 'name', ('age', 35), 'red', 'z'}
>>> T = (('name', 'anil'), ('age', 35))
>>> dict(T)
{'name': 'anil', 'age': 35}
>>> L = [1,2,3]
>>> s3.add(L)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s3.add(L)
TypeError: unhashable type: 'list'
>>> s3.add(s2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s3.add(s2)
TypeError: unhashable type: 'set'
>>> L.append(s3)
>>> L
[1, 2, 3, {'y', 'green', ('name', 'anil'), 'age', 'name', ('age', 35), 'red', 'z'}]
>>> s3
{'y', 'green', ('name', 'anil'), 'age', 'name', ('age', 35), 'red', 'z'}
>>> s3.remove('age')
>>> s3
{'y', 'green', ('name', 'anil'), 'name', ('age', 35), 'red', 'z'}
>>> s1.union(s2)
{'e', 'y', 'i', 'd', 'f', 'x', 'j', 'a', 'h', 'g', 'b', 'c', 'z'}
>>> s1.intersection(s2)
{'f', 'e', 'd', 'g'}
>>> #######################################################################
>>> 
>>> # Dictionaries
>>> D = {'name' : 'anil', 'age':35, 'country':'India'}
>>> D['name']
'anil'
>>> D['age']
35
>>> D['job']
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    D['job']
KeyError: 'job'
>>> D['job'] = 'Engineer'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'job': 'Engineer'}
>>> D['name'] = 'sunil'
>>> D
{'name': 'sunil', 'age': 35, 'country': 'India', 'job': 'Engineer'}
>>> D.setdefault('gender', 'M')
'M'
>>> D
{'name': 'sunil', 'age': 35, 'country': 'India', 'job': 'Engineer', 'gender': 'M'}
>>> D['addr']
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    D['addr']
KeyError: 'addr'
>>> D.setdefault('name')
'sunil'
>>> D['name']
'sunil'
>>> D['addr']
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    D['addr']
KeyError: 'addr'
>>> D.setdefault('addr')
>>> D
{'name': 'sunil', 'age': 35, 'country': 'India', 'job': 'Engineer', 'gender': 'M', 'addr': None}
>>> 'age' in D
True
>>> D.pop('addr')
>>> D
{'name': 'sunil', 'age': 35, 'country': 'India', 'job': 'Engineer', 'gender': 'M'}
>>> d1 = {'addr':'bangalore', 'userid':'sun998', 'psswd':'gyfu&*%'}
>>> D
{'name': 'sunil', 'age': 35, 'country': 'India', 'job': 'Engineer', 'gender': 'M'}
>>> D.update(d1)
>>> D
{'name': 'sunil', 'age': 35, 'country': 'India', 'job': 'Engineer', 'gender': 'M', 'addr': 'bangalore', 'userid': 'sun998', 'psswd': 'gyfu&*%'}
>>> D.items()
dict_items([('name', 'sunil'), ('age', 35), ('country', 'India'), ('job', 'Engineer'), ('gender', 'M'), ('addr', 'bangalore'), ('userid', 'sun998'), ('psswd', 'gyfu&*%')])
>>> D.keys()
dict_keys(['name', 'age', 'country', 'job', 'gender', 'addr', 'userid', 'psswd'])
>>> D.values()
dict_values(['sunil', 35, 'India', 'Engineer', 'M', 'bangalore', 'sun998', 'gyfu&*%'])
>>> 
