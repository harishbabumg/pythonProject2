Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
string = "Hai How are You"
dir(string)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
string
'Hai How are You'
string.lower()
'hai how are you'
string
'Hai How are You'
string.upper
<built-in method upper of str object at 0x000001E97100D0F0>
string.upper()
'HAI HOW ARE YOU'
string.swapcase()
'hAI hOW ARE yOU'
string
'Hai How are You'
string.count("a")
2
string.count(" ")
3
string.count("Hai")
1
string.count("Hai", 4, 7)
0
string.count("a", 3)
1
string.count("a", 3, 7)
0
string.count("a", 0)
2
string.index('a")
             
SyntaxError: unterminated string literal (detected at line 1)
string.index("a")
             
1
string.index("a", 0, 7)
             
1
string.index("a", 2)
             
8
string.find("a")
             
1
string.find("a", 2)
             
8
string.find("p")
             
-1
string.index("P")
             
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    string.index("P")
ValueError: substring not found
string
             
'Hai How are You'







































string.indec("a
             
SyntaxError: unterminated string literal (detected at line 1)
string.indec("a")
             
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    string.indec("a")
AttributeError: 'str' object has no attribute 'indec'. Did you mean: 'index'?
string.index("a")
             
1
string.rindex("a")
             
8
string.rindex("a", 2)
             
8
string.rfind("a")
             
8


string.rfind("a", 2)
             
8
string
             
'Hai How are You'


language = "Malayalam"
             

language.replace("a", "p")
             
'Mplpyplpm'
language
             
'Malayalam'
language.replace("a", "p", 2)
             
'Mplpyalam'
string
             
'Hai How are You'
string.replace("How", "who")
             
'Hai who are You'












string.startswith("ha")
             
False
string.startswith("Ha")
             
True
string.startswith("Ha", 4)
             
False
string.endswith("Ha")
             
False
string.endswith("You")
             
True
string.endswith("You", 4)
             
True

string.startswith("are", 11)
             
False
string.startswith("are", 8, 10)
             
False
string.startswith("are", 9, 11)
             
False
string
             
'Hai How are You'
string.startswith("are", 8, 12)
             
True
string.startswith("are", 8, 11)
             
True
string.startswith("are", 8, 10)
             
False














string
             
'Hai How are You'
string.split(" ")
             
['Hai', 'How', 'are', 'You']
word = "hello world"
             
word.spilt("o")
             
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    word.spilt("o")
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
word.spilt("o")
             
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    word.spilt("o")
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
word.split("o")
             
['hell', ' w', 'rld']
word.spilt("hello")
             
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    word.spilt("hello")
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?

word.split("hello")
             
['', ' world']
word.split("" ", 2)
           
SyntaxError: unterminated string literal (detected at line 1)
word.split(" ", 2)
           
['hello', 'world']
string.spilt(" ", 2)
           
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    string.spilt(" ", 2)
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
string.split(" ", 2)
           
['Hai', 'How', 'are You']
word.split("hello")
           
['', ' world']
word.split()
           
['hello', 'world']
string
           
'Hai How are You'
string.split("hai hello")
           
['Hai How are You']
string.split("hai How")
           
['Hai How are You']
word
           
'hello world'
word.split(w, 2)
           
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    word.split(w, 2)
NameError: name 'w' is not defined
word.split("w", 2)
           
['hello ', 'orld']
s = "hello world"
           







s.split()
           
['hello', 'world']
s.split(" ")
           
['hello', 'world']
"-".join(_)
           
'hello-world'
"-".join('hello', 'world')
           
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    "-".join('hello', 'world')
TypeError: str.join() takes exactly one argument (2 given)
'hello', 'world'
           
('hello', 'world')

"-".join(_)
           
'hello-world'


a = 'hai'
           
a
           
'hai'
a = "hai"
           
"#".join(a)
           
'h#a#i'
" ",join(a)
           
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    " ",join(a)
NameError: name 'join' is not defined
" ".join(a)
           
'h a i'
"hello".join(a)
           
'hhelloahelloi'
"*".join("o")
           
'o'
a
           
'hai'
a.spilt()
           
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a.spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
a.split()
           
['hai']
_
           
['hai']
