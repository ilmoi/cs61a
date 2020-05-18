from operator import add, sub, mul

# Link Class


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
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Tree Class


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

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

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


# naturals


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


# ==============================================================================


def prune_min(t):
    """Prune the tree mutatively from the bottom up.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    "*** YOUR CODE HERE ***"
    # my solution
    if not t.branches:
        return t
    else:
        min_b = min([b.label for b in t.branches])
        return Tree(t.label, [prune_min(b) for b in t.branches if b.label == min_b])

    # their solution - big difference is they're doing it in place, vs I returned
    if t.branches == []:
        return
    prune_min(t.branches[0])
    prune_min(t.branches[1])
    # you need the if construct because to mutate in place you're gonna have to use pop. Otherwise list comprehension would have been good enough
    if (t.branches[0].label > t.branches[1].label):
        t.branches.pop(0)
    else:
        t.branches.pop(1)


# t3 = Tree(6, [Tree(3, [Tree(2), Tree(1)]), Tree(2, [Tree(4), Tree(3)])])
# print(prune_min(t3))
# t2 = Tree(6, [Tree(3), Tree(4)])
# print(prune_min(t2))


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    # 4 times we're creating the high level generator:
    # 3 times we're iterating over the internal generator

    # mine
    # def inner_gen(i):
    #     nat = naturals()
    #     while True:
    #         x = next(nat)
    #         yield x * m + i - m

    # their
    def inner_gen(i):
        # definitely a much more natural approach
        for e in naturals():
            if e % m == i:
                yield e

    for i in range(m):
        yield inner_gen(i)


# remainders_four = remainders_generator(4)
# for i in range(4):
#     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
#     gen = next(remainders_four)  # gen = inner_gen()
#     for _ in range(3):
#         print(next(gen))


def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    else:
        return fn(link.first, foldr(link.rest, fn, z))


# lst = Link(3, Link(2, Link(1)))
# the reason the below prints out -6 is :0 -3 -2 -1
# print(foldl(lst, sub, 0))


def mapl(lst, fn):
    """ Maps FN on LST
    >>> lst = Link(3, Link(2, Link(1)))
    >>> mapl(lst, lambda x: x*x)
    Link(9, Link(4, Link(1)))
    """
    "*** YOUR CODE HERE ***"

    # first, here's the normal way you'd write it
    if lst is Link.empty:
        return Link.empty
    else:
        return Link(fn(lst.first), mapl(lst.rest, fn))

    # map with fold
    return foldr(lst, lambda x, xs: Link(fn(x), xs), Link.empty)


# lst = Link(3, Link(2, Link(1)))
# print(mapl(lst, lambda x: x*x))


def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return fn(foldl(link.rest, fn, z), link.first)


def filterl(lst, pred):
    """ Filters LST based on PRED
    >>> lst = Link(4, Link(3, Link(2, Link(1))))
    >>> filterl(lst, lambda x: x % 2 == 0)
    Link(4, Link(2))
    """
    "*** YOUR CODE HERE ***"
    # return foldr(lst, lambda x, xs: Link(fn(x), xs), Link.empty)
    return foldl(lst, pred, Link.empty)


lst = Link(4, Link(3, Link(2, Link(1))))
print(filterl(lst, lambda x, _: x % 2 == 0))


def reverse(lst):
    """ Reverses LST with foldl
    >>> reverse(Link(3, Link(2, Link(1))))
    Link(1, Link(2, Link(3)))
    >>> reverse(Link(1))
    Link(1)
    >>> reversed = reverse(Link.empty)
    >>> reversed is Link.empty
    True
    """
    "*** YOUR CODE HERE ***"


def identity(x): return x


def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
    return foldr(link, step, identity)(z)


def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    "*** YOUR CODE HERE ***"

    def difference_so_far(s, difference):
        if not s:
            if abs(difference) <= d:
                return 1
            else:
                return 0
        element = s[0]  # grab the first elem
        s = s[1:]  # truncate the list
        # same concept of "taking" and "not taking"
        # but instead of appending or not appending to lists they're appeneding or subtracting from difference - very smart
        # whenever the list is empty we'll have all opssible combination - and if at least one ends up with difference 0, then 1 is propagated all the way up
        return difference_so_far(s, difference + element) + difference_so_far(s, difference - element)
    # you get duplicates so you need to divide by 2!
    return difference_so_far(s, 0)//2
