"""
Linked lists are like trees - each element has a header (trees had labels, linked lists have "first") + potentially branches which must be trees / linked lists too.
"""
"""
foo = Foo('boo')
Foo.x
bam

foo.x
boo

foo.baz()
boo

Foo.baz()
error

Foo.baz(foo)
boo

bar = Bar('ang')

Bar.x
boom

bar.x
erang

bar.baz()
boom + erang


tim = Student(['Chem1A', 'Bio1B', 'CS61A', 'CS70', 'CogSci1'])
tim.make_friends()
creates a partner with subjects ['Bio1B', 'CS61A', 'CS70', 'CogSci1']

print(tim.subjects_to_take)
the above

tim.partner.make_friends()
creates a partner with subjects ['CS61A', 'CS70', 'CogSci1']

tim.take_course()
tim's courses are now like this: ['Chem1A', 'Bio1B', 'CS61A', 'CS70']
{CogSci: 4}
makes the above dude his partner ['CS61A', 'CS70', 'CogSci1']

tim.partner.take_course()
tim.take_course()
tim.make_friends()

"""
