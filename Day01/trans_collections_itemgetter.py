Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/Clients/IBM/Day01/randoms.py =====

RANDOMS:
[48, 100, 85, 38, 78, 19, 99, 36, 33, 14, 70, 67, 3, 43, 15, 8, 86, 35, 14, 71, 1, 27, 6, 16, 59, 47, 12, 55, 67, 35, 47, 95, 94, 91, 26, 22, 58, 41, 39, 8, 48, 67, 14, 22, 27, 64, 2, 11, 44, 80, 35, 79, 75, 79, 75, 14, 31, 100, 81, 67, 72, 63, 43, 41, 95, 100, 43, 88, 62, 21, 60, 12, 23, 4, 33, 40, 23, 7, 43, 58, 86, 90, 35, 57, 86, 81, 33, 95, 7, 82, 91, 82, 76, 91, 50, 96, 9, 42, 60, 51]

ODDS:
[85, 19, 99, 33, 67, 3, 43, 15, 35, 71, 1, 27, 59, 47, 55, 67, 35, 47, 95, 91, 41, 39, 67, 27, 11, 35, 79, 75, 79, 75, 31, 81, 67, 63, 43, 41, 95, 43, 21, 23, 33, 23, 7, 43, 35, 57, 81, 33, 95, 7, 91, 91, 9, 51]

EVENS:
[48, 100, 38, 78, 36, 14, 70, 8, 86, 14, 6, 16, 12, 94, 26, 22, 58, 8, 48, 14, 22, 64, 2, 44, 80, 14, 100, 72, 100, 88, 62, 60, 12, 4, 40, 58, 86, 90, 86, 82, 82, 76, 50, 96, 42, 60]
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/Clients/IBM/Day01/word_hist.py ====

Yeah
You are my fire
The one desire
Believe when I say
I want it that way
But we are two worlds apart
Can't reach to your heart
When you say
That I want it that way
Tell me why
Ain't nothin' but a heartache
Tell me why
Ain't nothin' but a mistake
Tell me why
I never want to hear you say
I want it that way
Am I, your fire?
Your one, desire
Yes I know, it's too late
But I want it that way
Tell me why
Ain't nothin' but a heartache
Tell me why
Ain't nothin' but a mistake
Tell me why,
I never want to hear you say
I want it that way
Now I can see that we've fallen apart
From the way that it used to be, yeah
No matter the distance
I want you to know
That deep down inside of me
You are my fire
The one desire
You are (you are, you are, you are)
Don't want to hear you say
Ain't nothin' but a heartache
Ain't nothin' but a mistake
(Don't want to hear you say)
I never want to hear you say
I want it that way
Tell me why
Ain't nothin' but a heartache
Tell me why
Ain't nothin' but a mistake
Tell me why
I never want to hear you say
I want it that way
Tell me why
Ain't nothin' but a heartache
Ain't nothin' but a mistake
Tell me why
I never want to hear you say
(Never want to hear you say it)
I want it that way
'Cause I want it that way


>>> type(text)
<class 'str'>
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/Clients/IBM/Day01/word_hist.py ====
{'Yeah': 1, 'You': 3, 'are': 4, 'my': 2, 'fire': 2, 'The': 2, 'one': 2, 'desire': 3, 'Believe': 1, 'when': 1, 'I': 18, 'say': 9, 'want': 18, 'it': 10, 'that': 11, 'way': 10, 'But': 2, 'we': 1, 'two': 1, 'worlds': 1, 'apart': 2, "Can't": 1, 'reach': 1, 'to': 11, 'your': 2, 'heart': 1, 'When': 1, 'you': 12, 'That': 2, 'Tell': 11, 'me': 12, 'why': 10, "Ain't": 10, "nothin'": 10, 'but': 10, 'a': 10, 'heartache': 5, 'mistake': 5, 'never': 5, 'hear': 8, 'Am': 1, 'I,': 1, 'fire?': 1, 'Your': 1, 'one,': 1, 'Yes': 1, 'know,': 1, "it's": 1, 'too': 1, 'late': 1, 'why,': 1, 'Now': 1, 'can': 1, 'see': 1, "we've": 1, 'fallen': 1, 'From': 1, 'the': 2, 'used': 1, 'be,': 1, 'yeah': 1, 'No': 1, 'matter': 1, 'distance': 1, 'know': 1, 'deep': 1, 'down': 1, 'inside': 1, 'of': 1, '(you': 1, 'are,': 2, 'are)': 1, "Don't": 1, "(Don't": 1, 'say)': 1, '(Never': 1, 'it)': 1, "'Cause": 1}
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/Clients/IBM/Day01/word_hist.py ====
{'red': 3, 'green': 2, 'yellow': 1}
>>> from collection import Counter
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from collection import Counter
ModuleNotFoundError: No module named 'collection'
>>> from collections import Counter
>>> z = Counter(text)
>>> z
Counter({'e': 8, 'r': 5, ' ': 5, 'd': 3, 'g': 2, 'n': 2, 'l': 2, 'y': 1, 'o': 1, 'w': 1})
>>> text
'red red red green green yellow'
>>> z = Counter(text.split())
>>> z
Counter({'red': 3, 'green': 2, 'yellow': 1})
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/Clients/IBM/Day01/word_hist.py ====
{'Yeah': 1, 'You': 3, 'are': 4, 'my': 2, 'fire': 2, 'The': 2, 'one': 2, 'desire': 3, 'Believe': 1, 'when': 1, 'I': 18, 'say': 9, 'want': 18, 'it': 10, 'that': 11, 'way': 10, 'But': 2, 'we': 1, 'two': 1, 'worlds': 1, 'apart': 2, "Can't": 1, 'reach': 1, 'to': 11, 'your': 2, 'heart': 1, 'When': 1, 'you': 12, 'That': 2, 'Tell': 11, 'me': 12, 'why': 10, "Ain't": 10, "nothin'": 10, 'but': 10, 'a': 10, 'heartache': 5, 'mistake': 5, 'never': 5, 'hear': 8, 'Am': 1, 'I,': 1, 'fire?': 1, 'Your': 1, 'one,': 1, 'Yes': 1, 'know,': 1, "it's": 1, 'too': 1, 'late': 1, 'why,': 1, 'Now': 1, 'can': 1, 'see': 1, "we've": 1, 'fallen': 1, 'From': 1, 'the': 2, 'used': 1, 'be,': 1, 'yeah': 1, 'No': 1, 'matter': 1, 'distance': 1, 'know': 1, 'deep': 1, 'down': 1, 'inside': 1, 'of': 1, '(you': 1, 'are,': 2, 'are)': 1, "Don't": 1, "(Don't": 1, 'say)': 1, '(Never': 1, 'it)': 1, "'Cause": 1}
>>> D
{'Yeah': 1, 'You': 3, 'are': 4, 'my': 2, 'fire': 2, 'The': 2, 'one': 2, 'desire': 3, 'Believe': 1, 'when': 1, 'I': 18, 'say': 9, 'want': 18, 'it': 10, 'that': 11, 'way': 10, 'But': 2, 'we': 1, 'two': 1, 'worlds': 1, 'apart': 2, "Can't": 1, 'reach': 1, 'to': 11, 'your': 2, 'heart': 1, 'When': 1, 'you': 12, 'That': 2, 'Tell': 11, 'me': 12, 'why': 10, "Ain't": 10, "nothin'": 10, 'but': 10, 'a': 10, 'heartache': 5, 'mistake': 5, 'never': 5, 'hear': 8, 'Am': 1, 'I,': 1, 'fire?': 1, 'Your': 1, 'one,': 1, 'Yes': 1, 'know,': 1, "it's": 1, 'too': 1, 'late': 1, 'why,': 1, 'Now': 1, 'can': 1, 'see': 1, "we've": 1, 'fallen': 1, 'From': 1, 'the': 2, 'used': 1, 'be,': 1, 'yeah': 1, 'No': 1, 'matter': 1, 'distance': 1, 'know': 1, 'deep': 1, 'down': 1, 'inside': 1, 'of': 1, '(you': 1, 'are,': 2, 'are)': 1, "Don't": 1, "(Don't": 1, 'say)': 1, '(Never': 1, 'it)': 1, "'Cause": 1}
>>> D.items()
dict_items([('Yeah', 1), ('You', 3), ('are', 4), ('my', 2), ('fire', 2), ('The', 2), ('one', 2), ('desire', 3), ('Believe', 1), ('when', 1), ('I', 18), ('say', 9), ('want', 18), ('it', 10), ('that', 11), ('way', 10), ('But', 2), ('we', 1), ('two', 1), ('worlds', 1), ('apart', 2), ("Can't", 1), ('reach', 1), ('to', 11), ('your', 2), ('heart', 1), ('When', 1), ('you', 12), ('That', 2), ('Tell', 11), ('me', 12), ('why', 10), ("Ain't", 10), ("nothin'", 10), ('but', 10), ('a', 10), ('heartache', 5), ('mistake', 5), ('never', 5), ('hear', 8), ('Am', 1), ('I,', 1), ('fire?', 1), ('Your', 1), ('one,', 1), ('Yes', 1), ('know,', 1), ("it's", 1), ('too', 1), ('late', 1), ('why,', 1), ('Now', 1), ('can', 1), ('see', 1), ("we've", 1), ('fallen', 1), ('From', 1), ('the', 2), ('used', 1), ('be,', 1), ('yeah', 1), ('No', 1), ('matter', 1), ('distance', 1), ('know', 1), ('deep', 1), ('down', 1), ('inside', 1), ('of', 1), ('(you', 1), ('are,', 2), ('are)', 1), ("Don't", 1), ("(Don't", 1), ('say)', 1), ('(Never', 1), ('it)', 1), ("'Cause", 1)])
>>> L = list(D.items())
>>> L
[('Yeah', 1), ('You', 3), ('are', 4), ('my', 2), ('fire', 2), ('The', 2), ('one', 2), ('desire', 3), ('Believe', 1), ('when', 1), ('I', 18), ('say', 9), ('want', 18), ('it', 10), ('that', 11), ('way', 10), ('But', 2), ('we', 1), ('two', 1), ('worlds', 1), ('apart', 2), ("Can't", 1), ('reach', 1), ('to', 11), ('your', 2), ('heart', 1), ('When', 1), ('you', 12), ('That', 2), ('Tell', 11), ('me', 12), ('why', 10), ("Ain't", 10), ("nothin'", 10), ('but', 10), ('a', 10), ('heartache', 5), ('mistake', 5), ('never', 5), ('hear', 8), ('Am', 1), ('I,', 1), ('fire?', 1), ('Your', 1), ('one,', 1), ('Yes', 1), ('know,', 1), ("it's", 1), ('too', 1), ('late', 1), ('why,', 1), ('Now', 1), ('can', 1), ('see', 1), ("we've", 1), ('fallen', 1), ('From', 1), ('the', 2), ('used', 1), ('be,', 1), ('yeah', 1), ('No', 1), ('matter', 1), ('distance', 1), ('know', 1), ('deep', 1), ('down', 1), ('inside', 1), ('of', 1), ('(you', 1), ('are,', 2), ('are)', 1), ("Don't", 1), ("(Don't", 1), ('say)', 1), ('(Never', 1), ('it)', 1), ("'Cause", 1)]
>>> from operator import itemgetter
>>> f = itemgetter(1)
>>> f('sleep')
'l'
>>> f([10, 20, 30])
20
>>> f(('Yeah', 1))
1
>>> L.sort(key=f)
>>> L
[('Yeah', 1), ('Believe', 1), ('when', 1), ('we', 1), ('two', 1), ('worlds', 1), ("Can't", 1), ('reach', 1), ('heart', 1), ('When', 1), ('Am', 1), ('I,', 1), ('fire?', 1), ('Your', 1), ('one,', 1), ('Yes', 1), ('know,', 1), ("it's", 1), ('too', 1), ('late', 1), ('why,', 1), ('Now', 1), ('can', 1), ('see', 1), ("we've", 1), ('fallen', 1), ('From', 1), ('used', 1), ('be,', 1), ('yeah', 1), ('No', 1), ('matter', 1), ('distance', 1), ('know', 1), ('deep', 1), ('down', 1), ('inside', 1), ('of', 1), ('(you', 1), ('are)', 1), ("Don't", 1), ("(Don't", 1), ('say)', 1), ('(Never', 1), ('it)', 1), ("'Cause", 1), ('my', 2), ('fire', 2), ('The', 2), ('one', 2), ('But', 2), ('apart', 2), ('your', 2), ('That', 2), ('the', 2), ('are,', 2), ('You', 3), ('desire', 3), ('are', 4), ('heartache', 5), ('mistake', 5), ('never', 5), ('hear', 8), ('say', 9), ('it', 10), ('way', 10), ('why', 10), ("Ain't", 10), ("nothin'", 10), ('but', 10), ('a', 10), ('that', 11), ('to', 11), ('Tell', 11), ('you', 12), ('me', 12), ('I', 18), ('want', 18)]
>>> L.sort(key=f, reverse=True)
>>> L
[('I', 18), ('want', 18), ('you', 12), ('me', 12), ('that', 11), ('to', 11), ('Tell', 11), ('it', 10), ('way', 10), ('why', 10), ("Ain't", 10), ("nothin'", 10), ('but', 10), ('a', 10), ('say', 9), ('hear', 8), ('heartache', 5), ('mistake', 5), ('never', 5), ('are', 4), ('You', 3), ('desire', 3), ('my', 2), ('fire', 2), ('The', 2), ('one', 2), ('But', 2), ('apart', 2), ('your', 2), ('That', 2), ('the', 2), ('are,', 2), ('Yeah', 1), ('Believe', 1), ('when', 1), ('we', 1), ('two', 1), ('worlds', 1), ("Can't", 1), ('reach', 1), ('heart', 1), ('When', 1), ('Am', 1), ('I,', 1), ('fire?', 1), ('Your', 1), ('one,', 1), ('Yes', 1), ('know,', 1), ("it's", 1), ('too', 1), ('late', 1), ('why,', 1), ('Now', 1), ('can', 1), ('see', 1), ("we've", 1), ('fallen', 1), ('From', 1), ('used', 1), ('be,', 1), ('yeah', 1), ('No', 1), ('matter', 1), ('distance', 1), ('know', 1), ('deep', 1), ('down', 1), ('inside', 1), ('of', 1), ('(you', 1), ('are)', 1), ("Don't", 1), ("(Don't", 1), ('say)', 1), ('(Never', 1), ('it)', 1), ("'Cause", 1)]
>>> 
