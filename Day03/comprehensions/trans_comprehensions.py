Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = []
>>> for i in range(100):
	if( i%7 == 0 ):
		s.append(i)

		
>>> s
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
>>> L = [x for x in range(100) (if x % 7 == 0)]
SyntaxError: invalid syntax
>>> L = [x for x in range(100) if (x % 7 == 0)]
>>> L
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
>>> T = (x**2 for x in range(10))
>>> T
<generator object <genexpr> at 0x0000022BB4076930>
>>> tuple(T)
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
>>> words = ['apples', 'banana', 'cattle', 'donkey', 'elephant']
>>> dw = {key:len(key) for key in words}
>>> dw
{'apples': 6, 'banana': 6, 'cattle': 6, 'donkey': 6, 'elephant': 8}
>>> from collections import Counter
>>> dw = {key:(len(key), Counter(key)) for key in words}
>>> dw
{'apples': (6, Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1, 's': 1})), 'banana': (6, Counter({'a': 3, 'n': 2, 'b': 1})), 'cattle': (6, Counter({'t': 2, 'c': 1, 'a': 1, 'l': 1, 'e': 1})), 'donkey': (6, Counter({'d': 1, 'o': 1, 'n': 1, 'k': 1, 'e': 1, 'y': 1})), 'elephant': (8, Counter({'e': 2, 'l': 1, 'p': 1, 'h': 1, 'a': 1, 'n': 1, 't': 1}))}
>>> L = [(x, y) for x in range(10) for y in range(10) if (x + y > 10)]
>>> L
[(2, 9), (3, 8), (3, 9), (4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
>>> words
['apples', 'banana', 'cattle', 'donkey', 'elephant']
>>> capwords = [w.capitalize() for w in words]
>>> capwords
['Apples', 'Banana', 'Cattle', 'Donkey', 'Elephant']
>>> capwords = [w.capitalize for w in words if w.startswith('c')]
>>> capwords
[<built-in method capitalize of str object at 0x0000022BB40B6DC0>]
>>> list(capwords)
[<built-in method capitalize of str object at 0x0000022BB40B6DC0>]
>>> capwords = [w.capitalize() for w in words if w.startswith('c')]
>>> capwords
['Cattle']
>>> capwords = [w.upper() if w.startswith('c') else w for w in words]
>>> capwords
['apples', 'banana', 'CATTLE', 'donkey', 'elephant']
>>> words
['apples', 'banana', 'cattle', 'donkey', 'elephant']
>>> revwords = [w[::-1] for w in words]
>>> revwords
['selppa', 'ananab', 'elttac', 'yeknod', 'tnahpele']
>>> 
