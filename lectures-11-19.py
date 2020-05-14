import operator


def factors(n):
    """Finds out the factors of n."""
    i = 1
    total = 0
    while i <= n:
        if n % i == 0:
            total += 1
        i += 1
    return total


print(factors(28))


def sqrt_factors(n):
    """Same as above but we're more efficient since we figured out that each factor actually automatically reveals two factos"""
    """In this way reduce complexity from n to sqrt(n)"""
    i = 1
    total = 0
    while i**2 <= n:  # note now we're using a square here!
        if n % i == 0:
            total += 2  # note 2 not 1 here!
        i += 1
    if i**2 == n:
        total += 1
    return total


print(sqrt_factors(28))


def exp_slow(b, n):
    """Raises b to the power of n"""
    if n == 0:
        return 1
    else:
        return b * exp_slow(b, n-1)


print(exp_slow(2, 3))


def exp_fast(b, n):
    """Raises b to the power of n but quicker"""
    if n == 0:
        return 1  # the same
    elif n % 2 == 0:
        return (exp_fast(b, n//2))**2  # square on the outside and //2 on the inside cancel out
    else:
        return b * exp_fast(b, n-1)


print(exp_fast(2, 3))


print("-------------------- 16 Mutables Trees --------------------")

# ==============================================================================
# old, ADT implementation


def label(tree):
    """Abstract datatype tree LABEL SELECTOR"""
    return tree[0]


def branches(tree):
    """Abstract datatype tree BRANCHES SELECTOR"""
    return tree[1:]  # IMPORTANT: [1:] not [1]. In this way we're saying 1st item onwards, and if 1st item (ie branches) is empty it will return an EMPTY list [], not an error


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True  # yes you need this


def is_leaf(tree):
    return not branches(tree)


def tree(label, branches=[]):
    """Abstract datatype tree CONSTRUCTOR"""

    for b in branches:
        assert is_tree(b), 'branches must be trees'

    return [label] + list(branches)


# ==============================================================================
# new, class implementation

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        self.label = fn(self.label)
        for b in self.branches:
            # b.label = fn(b.label) #THIS IS NOT RECURSIVE, FAILS
            b.map(fn)  # this is recursive

    def __contains__(self, e):
        """Checks if a given element is present in the class."""
        # note this is the magic method for "in", eg "2 in t"
        if self.label == e:
            return True
        for b in branches:
            if b.__contains__(e):
                return True
        return False  # don't forget this one


t = Tree(3, [Tree(1),
             Tree(2, [Tree(1),
                      Tree(1)])])


print(t.is_leaf())
print(t.branches[0].is_leaf())


# differences between abstract data type (ADT) representation and a class-based representation
# we can assign a new label to a class easily - but we can't do that with a function call
t.label = 555
print(t.label)

# note with a lowercase t
tt = tree(3, [tree(1),
              tree(2, [tree(1),
                       tree(1)])])

# tt.label = 555  # produces an error
# to change the label I would have to basically re-create the tree using a diff label:


def change_label(tt, new_lab):
    if is_leaf(tt):
        return tt
    else:
        return tree(new_lab, [b for b in branches(tt)])


print(change_label(tt, 555))


# NOTE: this is why classes are a much better choice for MUTABLE datatypes!!!
# NOTE 2: think about what mutability even means - it means changing in place. Classes let us do that, functions do not


t.map(lambda x: x*100)
print(t.label, t.branches[1].label, t.branches[1].branches[0].label)


# ==============================================================================
# Binary Search Trees (BSTs) - trees where each node has at most 2 branches
# left branch = only elements that are less than or equal to the label
# right branch = only elements that are greater than the label
# it's a RECURSIVE structure, so left and right branches are themselves BSTs

class BST:
    empty = ()  # note how we introduce our own definiton of empty right at the top of the class

    def __init__(self, label, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)
        self.label = label
        self.left = left
        self.right = right

        if left is not BST.empty:
            assert left.max() <= label
        if right is not BST.empty:
            assert label < right.min()

    def min(self):
        # My initial version - but it's actually unnecessary complex!
        # if self.is_leaf():
        #     return self.label
        # return min(self.left.min(), self.right.min())

        if self.left is BST.empty:  # this is neat - we know how the tree is ordered and can make use of that. everything in right branch is bigger than the label so we don't need to check it
            return self.label
        return self.left.min()

    def max(self):
        if self.right is BST.empty:
            return self.label
        return self.right.max()

    def is_leaf(self):
        # this is a beter way to write it than using an if statement - AND just marries two T/F
        return left is BST.empty() and right is BST.empty()

    def __contains__(self, e):
        # we can perform a more INTELLIGENT search here since we know the ordering of branches
        if self.label == e:
            return True
        elif e > self.label and self.right is not BST.empty:
            return self.right.__contains__(e)
        elif self.left is not BST.empty:  # we should be checking this otherwise we'll produce an error
            return self.left.__contains__(e)


b = BST(6,
        left=BST(2,
                 left=BST(1),
                 right=BST(4)),
        right=BST(7,
                  right=BST(9)))  # note this HAS to be right branch, since it's bigger than the parent label


# NOTE how the complexity on this search is log(n) vs on a normal tree where the complexity is just n
print(2 in b)


print("-------------------- 18 - Generators --------------------")


def countdown(k):
    """Returns a generator that counts down from k."""

    # one way of doing it
    # yield from reversed(range(k))

    # another way
    # base case
    if k == 0:
        yield "blast off!"
    else:
        yield k
        yield from countdown(k-1)


k = countdown(3)
print(next(k))
print(next(k))
print(next(k))
print(next(k))


print("-------------------- 19 Tail recursion --------------------")

# non tail form (normal recursion)


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


def tail_factorial(n, accumulator=1):
    """IN THEORY this is an optimzied version of the factorial function above (wait for it).
    Because we return ONLY the result of calling the function itself (without the added multiplication), it can be optimized.
    Specifically: because we're not doing anything to the inside function call other than returning it - we could THROW AWAY all the intermediate frames and only keep track of the last one.
    In this way we could take our space complexity from O(n) to O(1).
    EXCEPT - python doesn't support this. Python as a language was built more around iteration than around recursion. Eg it only supports around 1000 recursive calls before it maxes out.
    So this is actually bullshit. It's no better than the above:)
    But you get the idea.

    If you're really desperate for tail recursion - this guy built a creative workaround https://chrispenner.ca/posts/python-tail-recursion
    """
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n-1, accumulator * n)  # NOTE: no multiplication


print(factorial(5))
print(tail_factorial(5))

# get python dictionary sorted by values
dict = {
    'one': 'a',
    'not_two': 'c',
    'not_three': 'b'
}

sorted_dict = sorted(dict.items(), key=lambda x: x[1])
sorted_dict2 = sorted(dict.items(), key=operator.itemgetter(1))

print(sorted_dict)
print(sorted_dict2)

# how to merge two dicts
a = {1: 1, 2: 2}
b = {3: 3, 4: 4}
c = {**a, **b}
print(c)
