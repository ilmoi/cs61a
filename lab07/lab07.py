""" Lab 07: Generators, Linked Lists, and Trees """


# Linked Lists

def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"

# Trees


def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"

# Link List Class


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        # nice - very neat repr function that makes use of recursion
        # repr(self.first) refers to repr of just a string, so it'll just print out the string
        # rept(self.rest) refers to repr of another Link object (if not empty), and so it will recurse back to this same function
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            # nice here we use iteration to add strings together into a single one
            # NO recursion! self.first is just a string
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# link = Link(1000, Link()) #ERROR because second Link missing an arg

# link = Link(1, Link(2))
# link.first = 900
# print(link.first)
#
# link = Link(1)
# print(link)
# # ok fascinating, I didn't realize this but you CAN have a class recursively link to itself as an attribute. We can keep going with the below forever!
# link.rest = link
# print(link.rest.first)
# print(link.rest.rest.first)
# print(link.rest.rest.rest.first)
# print(link.rest.rest.rest.rest.first)

def link_to_list(link):

    nums = []

    while link is not Link.empty:
        nums.append(link.first)
        link = link.rest

    return nums


link = Link(1, Link(2, Link(3, Link(4))))
print(link_to_list(link))
print(link_to_list(Link.empty))

# ==============================================================================
# Tree ADT


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"


def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"


def cumulative_mult(t):
    """Mutates the tree so that each node's label becomes the product of all labels in the subtree rooted at node."""

    if t.is_leaf():
        return Tree(t.label)

    # MY VERSION
    # my understanding is that you a)count the label, b)only count first level of branches, not recursively
    # total = t.label
    # for b in t.branches:
    #     total *= cumulative_mult(b).label
    #     print(f'running total is {total}')
    #
    # # feels weird that I have to recurse twice
    # return Tree(total, branches=[cumulative_mult(b) for b in t.branches])

    # THEIR VERSION
    # transforms the branches FIRST
    for b in t.branches:
        cumulative_mult(b)
    # then do the total
    total = t.label
    for b in t.branches:
        total *= b.label
    t.label = total
    return t


# t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
# print(cumulative_mult(t))

print("--------------------  --------------------")


def seq_in_link(link, sub_link):
    """Returns true if sub_link found inside of link (not necessarily sequentially)"""

    # here's a real shitty solution

    def seq_extractor(link):
        seq = ""
        while link is not Link.empty:
            seq += str(link.first)
            link = link.rest
        return seq

    big = seq_extractor(link)
    small = seq_extractor(sub_link)

    print(big, small)

    total_yes = 0
    for i in range(-1, -len(small)-1, -1):
        for j in range(-1, -len(big)-1, -1):
            if small[i] == big[j]:
                total_yes += 1
                big = big[:j]
                print(f'new big is {big}')
                break

    return total_yes == len(small)


def seq_in_link(link, sub_link):
    if sub_link is Link.empty:
        return True
    if link is Link.empty:
        return False
    if link.first == sub_link.first:
        return seq_in_link(link.rest, sub_link.rest)
    else:
        return seq_in_link(link.rest, sub_link)
    # fuck this is so obvious. I made the mistake of thinking I need to check last digits first when it's actually much easier to check first digits first


lnk1 = Link(1, Link(2, Link(3, Link(4))))
lnk2 = Link(1, Link(3))
print(seq_in_link(lnk1, lnk2))
