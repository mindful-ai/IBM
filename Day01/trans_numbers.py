Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello IBM!')
Hello IBM!
>>> # Numbers
>>> a = 10
>>> b = 20
>>> type(a)
<class 'int'>
>>> c = 2.34
>>> type(c)
<class 'float'>
>>> a + b
30
>>> a / b
0.5
>>> a // b
0
>>> 3 // 2
1
>>> 3 % 2
1
>>> 2 / 2
1.0
>>> 3 / 2
1.5
>>> a * b
200
>>> a ** 2
100
>>> a > b
False
>>> a <= b
True
>>> d = True
>>> type(d)
<class 'bool'>
>>> a > b/2
False
>>> a == b * 2
False
>>> a
10
>>> b
20
>>> a == b * 2
False
>>> b * 2
40
>>> b == a * 2
True
>>> a > b and b < 30
False
>>> a < b and b <= 20
True
>>> int('188')
188
>>> s = '188'
>>> type(s)
<class 'str'>
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
198
>>> input('Enter a number: ')
Enter a number: 213
'213'
>>> s = input('Enter a number: ')
Enter a number: 213
>>> s
'213'
>>> int(s)
213
>>> float(s)
213.0
>>> s1 = input('Enter the value of pi: ')
Enter the value of pi: 3.14
>>> s1
'3.14'
>>> c = 2 * int(s1) * 5
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c = 2 * int(s1) * 5
ValueError: invalid literal for int() with base 10: '3.14'
>>> 
KeyboardInterrupt
>>> c = 2 * float(s1) * 5
>>> c
31.400000000000002
>>> i = 34.56
>>> int(i)
34
>>> i = '34.56'
>>> int(i)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(i)
ValueError: invalid literal for int() with base 10: '34.56'
>>> bin(100)
'0b1100100'
>>> hex(100)
'0x64'
>>> oct(100)
'0o144'
>>> i = '1101'
>>> int(i)
1101
>>> int(i, 2)
13
>>> int('0x64')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int('0x64')
ValueError: invalid literal for int() with base 10: '0x64'
>>> int('0x64', 16)
100
>>> a - b
-10
>>> abs(a - b)
10
>>> # https://docs.python.org/3/library/
>>> 
>>> 
>>> sqrt(10)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sqrt(10)
NameError: name 'sqrt' is not defined
>>> import math
>>> math.sqrt(100)
10.0
>>> math.gcd(10, 20)
10
>>> math.factorial(5)
120
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14156/180)
0.9999999998667178
>>> math.sin(math.radians(90))
1.0
>>> math.sin(90 * math.pi/180)
1.0
>>> import random
>>> random.randint(1, 100)
25
>>> random.randint(1, 100)
41
>>> random.randint(1, 100)
6
>>> random.randint(1, 100)
75
>>> random.randint(1, 100)
17
>>> random.randint(1, 100)
26
>>> random.randint(1, 100)
92
>>> 
