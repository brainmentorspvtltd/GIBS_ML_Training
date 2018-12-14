Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = ['hello','python',101,102,120.23,True]
>>> type(x)
<class 'list'>
>>> x = 'hello','python',101,102,120.23,True
>>> type(x)
<class 'tuple'>
>>> x[0]
'hello'
>>> x = ['hello','python',101,102,120.23,True]
>>> x[0]
'hello'
>>> x[5]
True
>>> x.append('Ravi')
>>> x
['hello', 'python', 101, 102, 120.23, True, 'Ravi']
>>> x.append('Amit','Ram','Shyam')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.append('Amit','Ram','Shyam')
TypeError: append() takes exactly one argument (3 given)
>>> x
['hello', 'python', 101, 102, 120.23, True, 'Ravi']
>>> x.insert(3,'AI')
>>> x
['hello', 'python', 101, 'AI', 102, 120.23, True, 'Ravi']
>>> x[-1]
'Ravi'
>>> y = []
>>> for i in range(1,51):
	if i % 2 == 0:
		y.append(i)

		
>>> y
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> y = [i for i in range(1,51) if i%2 == 0]
>>> y
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> import random
>>> random.shuffle(y)
>>> y
[26, 14, 48, 30, 34, 50, 20, 36, 46, 40, 42, 18, 38, 8, 24, 6, 10, 12, 4, 16, 32, 44, 22, 2, 28]
>>> sorted(y)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> sorted(y, reversed=True)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sorted(y, reversed=True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> sorted(y, reverse=True)
[50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
>>> y.sort()
>>> y
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> y[0:6]
[2, 4, 6, 8, 10, 12]
>>> y[0:20:2]
[2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
>>> y[0:1]
[2]
>>> y[0:10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> y[10:0]
[]
>>> y[0:10:1]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> y[10:0:-1]
[22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
>>> y[-1:-10]
[]
>>> y[-1:-10:-1]
[50, 48, 46, 44, 42, 40, 38, 36, 34]
>>> y = (50, 48, 46, 44, 42, 40, 38, 36, 34)
>>> y[0] = 12
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    y[0] = 12
TypeError: 'tuple' object does not support item assignment
>>> emp = {'name':'Ram','company':'tcs','dept':'HR'}
>>> emp['salary'] = 25000
>>> emp
{'name': 'Ram', 'company': 'tcs', 'dept': 'HR', 'salary': 25000}
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['name']
'Ram'
>>> emp.items()
dict_items([('name', 'Ram'), ('company', 'tcs'), ('dept', 'HR'), ('salary', 25000)])
>>> emp.keys()
dict_keys(['name', 'company', 'dept', 'salary'])
>>> emp.values()
dict_values(['Ram', 'tcs', 'HR', 25000])
>>> s1 = {2,3,4,5,6,1,12,23,11,12,2,4,56,23,3}
>>> s1
{1, 2, 3, 4, 5, 6, 11, 12, 23, 56}
>>> s2 = {45,34,12,11,40,3,5,7}
>>> s1 & s2
{11, 3, 12, 5}
>>> s1.intersection(s2)
{11, 3, 12, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 34, 7, 40, 11, 12, 45, 23, 56}
>>> s1 - s2
{1, 2, 4, 6, 23, 56}
>>> 
