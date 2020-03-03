Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> s + ' perl'
'python perl'
>>> s * 3
'pythonpythonpython'
>>> 'th' in s
True
>>> len(s)
6
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 'python'
>>> s[0]
'p'
>>> s[4]
'o'
>>> s[1:5]
'ytho'
>>> s[1:5:2]
'yh'
>>> s[:3]
'pyt'
>>> s[3:]
'hon'
>>> s[-1]
'n'
>>> s[-3:-1]
'ho'
>>> s[:]
'python'
>>> s[::2]
'pto'
>>> s[::-1]
'nohtyp'
>>> s[2:5:-1]
''
>>> s[2:5][::-1]
'oht'
>>> s[::-2]
'nhy'
>>> # fuctions related to case of the string
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> # functions to query the string
>>> s1 = '123'
>>> s2 = '123a'
>>> s3 = ' '
>>> s4 = 'dsf'
>>> s5 = '&^*&'
>>> s1.isdigit()
True
>>> s2.isalnum()
True
>>> s4.isalpha()
True
>>> s3.isspace()
True
>>> s5.isalpha()
False
>>> site = 'www.ibm.com'
>>> type(site)
<class 'str'>
>>> site.startswith('www')
True
>>> site.endswith('org')
False
>>> # modifying strings
>>> s = 'This is a test case
SyntaxError: EOL while scanning string literal
>>> s = 'This is a test case'
>>> s[0] = 'H'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s[0] = 'H'
TypeError: 'str' object does not support item assignment
>>> s.split()
['This', 'is', 'a', 'test', 'case']
>>> s.split('s')
['Thi', ' i', ' a te', 't ca', 'e']
>>> L = ['Python', 'Class']
>>> ' '.join(L)
'Python Class'
>>> L = s.split()
>>> L
['This', 'is', 'a', 'test', 'case']
>>> '-'.join(L)
'This-is-a-test-case'
>>> ip = '192-168-3.1'
>>> L.join()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    L.join()
AttributeError: 'list' object has no attribute 'join'
>>> s
'This is a test case'
>>> s + ' #1'
'This is a test case #1'
>>> s
'This is a test case'
>>> s2 = s + ' #1'
>>> s2
'This is a test case #1'
>>> s = s + ' #1'
>>> s
'This is a test case #1'
>>> ip
'192-168-3.1'
>>> ip.replace('-', '.')
'192.168.3.1'
>>> s = '  python  '
>>> s.strip()
'python'
>>> s.lstrip()
'python  '
>>> s.rstrip()
'  python'
>>> # seraching
>>> s
'  python  '
>>> s.find('tho')
4
>>> 'tho' in s
True
>>> 
