Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Lists
>>> L = ['red', 'green', 'blue']
>>> type(L)
<class 'list'>
>>> L1 = ['cyan', 'magenta', 'black']
>>> # Operators
>>> L + L1
['red', 'green', 'blue', 'cyan', 'magenta', 'black']
>>> L
['red', 'green', 'blue']
>>> L1
['cyan', 'magenta', 'black']
>>> L * 3
['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']
>>> 'red' in L
True
>>> 'black' in L + L1
True
>>> del L[0]
>>> L
['green', 'blue']
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> L = ['red', 'green', 'blue']
>>> len(L)
3
>>> ####### Replace
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue']
>>> L[0:2] = L1
>>> L
['cyan', 'magenta', 'black', 'blue']
>>> L[8]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    L[8]
IndexError: list index out of range
>>> ########## Accesability
>>> L[0]
'cyan'
>>> L[1:]
['magenta', 'black', 'blue']
>>> L[:]
['cyan', 'magenta', 'black', 'blue']
>>> L[::2]
['cyan', 'black']
>>> L[::-1]
['blue', 'black', 'magenta', 'cyan']
>>> ############## Functions
>>> L
['cyan', 'magenta', 'black', 'blue']
>>> L.append('red')
>>> L
['cyan', 'magenta', 'black', 'blue', 'red']
>>> L.append('green')
>>> L
['cyan', 'magenta', 'black', 'blue', 'red', 'green']
>>> L.insert(2, 'white')
>>> L
['cyan', 'magenta', 'white', 'black', 'blue', 'red', 'green']
>>> L2 = ['white', 'grey', 'black']
>>> L2
['white', 'grey', 'black']
>>> L.insert(1, L2)
>>> L
['cyan', ['white', 'grey', 'black'], 'magenta', 'white', 'black', 'blue', 'red', 'green']
>>> L + L2
['cyan', ['white', 'grey', 'black'], 'magenta', 'white', 'black', 'blue', 'red', 'green', 'white', 'grey', 'black']
>>> L
['cyan', ['white', 'grey', 'black'], 'magenta', 'white', 'black', 'blue', 'red', 'green']
>>> L[3] = L2
>>> L
['cyan', ['white', 'grey', 'black'], 'magenta', ['white', 'grey', 'black'], 'black', 'blue', 'red', 'green']
>>> L[4]
'black'
>>> L[4:5] = L2
>>> L
['cyan', ['white', 'grey', 'black'], 'magenta', ['white', 'grey', 'black'], 'white', 'grey', 'black', 'blue', 'red', 'green']
>>> L[1]
['white', 'grey', 'black']
>>> L[1][1]
'grey'
>>> L[1][1][-1]
'y'
>>> L2
['white', 'grey', 'black']
>>> L2.pop()
'black'
>>> L2
['white', 'grey']
>>> L2.pop()
'grey'
>>> L
['cyan', ['white'], 'magenta', ['white'], 'white', 'grey', 'black', 'blue', 'red', 'green']
>>> L2
['white']
>>> L2 = ['white', 'grey', 'black']
>>> L2
['white', 'grey', 'black']
>>> L2.pop(1)
'grey'
>>> L
['cyan', ['white'], 'magenta', ['white'], 'white', 'grey', 'black', 'blue', 'red', 'green']
>>> L2
['white', 'black']
>>> L.remove('black')
>>> L
['cyan', ['white'], 'magenta', ['white'], 'white', 'grey', 'blue', 'red', 'green']
>>> L2
['white', 'black']
>>> L2.remove('black')
>>> L2
['white']
>>> ###### Re-arranging elements of an array
>>> 
>>> L = ['goat', 'apples', 'cat', 'bells']
>>> sorted(L)
['apples', 'bells', 'cat', 'goat']
>>> L
['goat', 'apples', 'cat', 'bells']
>>> L.sort()
>>> L
['apples', 'bells', 'cat', 'goat']
>>> reversed(L)
<list_reverseiterator object at 0x000001BC6E88F6A0>
>>> list(reversed(L))
['goat', 'cat', 'bells', 'apples']
>>> L
['apples', 'bells', 'cat', 'goat']
>>> L.reverse()
>>> L
['goat', 'cat', 'bells', 'apples']
>>> ####### searching
>>> L
['goat', 'cat', 'bells', 'apples']
>>> 'bells' in L
True
>>> L.index('bells')
2
>>> L
['goat', 'cat', 'bells', 'apples']
>>> L.append('bells')
>>> L
['goat', 'cat', 'bells', 'apples', 'bells']
>>> L.count('bells')
2
>>> L3 = ['a', 'b', 1, 2]
>>> 2 in L
False
>>> 2 in L3
True
>>> C = [type(i) for i in L3]
>>> C
[<class 'str'>, <class 'str'>, <class 'int'>, <class 'int'>]
>>> type(5) = int
SyntaxError: can't assign to function call
>>> type(5) == '<class 'int'>'
SyntaxError: invalid syntax
>>> type(5) == '<class \'int\'>'
False
>>> 
