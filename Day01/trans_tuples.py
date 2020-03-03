Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tupes
>>> # Tuples
>>> T = ('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[:]
('red', 'green', 'blue')
>>> T[0] = 'orange'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    T[0] = 'orange'
TypeError: 'tuple' object does not support item assignment
>>> sorted(T)
['blue', 'green', 'red']
>>> reversed(T)
<reversed object at 0x0000021F74DC16D8>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> T1 = ('cyan', 'magenta')
>>> T1 + T
('cyan', 'magenta', 'red', 'green', 'blue')
>>> T
('red', 'green', 'blue')
>>> T1
('cyan', 'magenta')
>>> T2 *3
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    T2 *3
NameError: name 'T2' is not defined
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> T
('red', 'green', 'blue')
>>> 'red' in T
True
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
