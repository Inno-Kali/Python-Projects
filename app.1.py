>>> 4+5
9
>>> 4.0/3
1.3333333333333333
>>> 3+5/9
3
>>> ("abc" + "def")
'abcdef'
>>> ("hello

import math
rad = input("enter the radius ")
enter the radius >? 23
sa = 4*(22/7)*(rad*rad)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
rad = input("enter the radius ")
enter the radius >? 34
sa = 4*(22/7)*(rad*rad)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
type(rad)
<class 'str'>
rad = float(input("enter the radius "))
enter the radius >? 34
type(rad)
<class 'float'>
sa = 4*(22/7)*(rad*rad)
print (sa)
14532.571428571428
vol = (4/3)*(22/7)*pow(rad,3)
print (vol)
164702.47619047615
vol = (4/3)*(math.pi)*pow(rad,3)
print (sa)
14532.571428571428
rad = float(input("enter the radius "))
enter the radius >? 0.4
print (sa)
14532.571428571428
rad = float(input("enter the radius "))
enter the radius >? 0.3
0.3
0.3
sa = 4*(22/7)*(rad*rad)
print (sa)
1.1314285714285715
rad = float(input("enter the radius "))
enter the radius >? 0.8
vol = (4/3)*(math.pi)*pow(rad,3)
print (sa)
1.1314285714285715
print (sa + " and "+  vol)