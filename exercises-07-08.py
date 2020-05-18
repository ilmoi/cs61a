"""
>>> from lab07 import *
nothing
>>> link = Link(1000)
nothing
>>> link.first
1000
______

>>> link.rest is Link.empty
true
______

>>> link = Link(1000, 2000)
error, rest has to be either empty or a string
______

>>> link = Link(1000, Link())
nothing

______
>>> from lab07 import *
nothing
>>> link = Link(1, Link(2, Link(3)))
nothing
>>> link.first
1

______

>>> link.rest.first
2
______

>>> link.rest.rest.rest is Link.empty
true

______

>>> link.first = 9001
nothing
>>> link.first
9001

______

>>> link.rest = link.rest.rest
nothing
>>> link.rest.first
3

______

>>> link = Link(1)
nothing
>>> link.rest = link
nothing
>>> link.rest.rest.rest.rest.first
error

______

>>> link = Link(2, Link(3, Link(4)))
nothing
>>> link2 = Link(1, link)
nothing
>>> link2.first
1
______

>>> link2.rest.first
2

______
>>> from lab07 import *
>>> link = Link(5, Link(6, Link(7)))
>>> link                  # Look at the __repr__ method of Link
returns exactly the above
______

>>> print(link)          # Look at the __str__ method of Link
returns <5 6 7 >
______
"""

print("-------------------- Discussion 08 --------------------")
