# ==============================================================================
# Tree stuff from before


import itertools


def label(tree):
    """Abstract datatype tree LABEL SELECTOR"""
    return tree[0]


def branches(tree):
    """Abstract datatype tree BRANCHES SELECTOR"""
    return tree[1:]  # IMPORTANT: [1:] not [1]. In this way we're saying 1st item onwards, and if 1st item (ie branches) is empty it will return an EMPTY list [], not an error


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    # then for each branch we check again, recursively
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True  # yes you need this


def is_leaf(tree):
    # how not works: takes branches > if empty, returns True, else False
    return not branches(tree)


def tree(label, branches=[]):
    """Abstract datatype tree CONSTRUCTOR"""
    # if the tree is a leaf, then the branches list would be empty

    for b in branches:
        # print(b)
        assert is_tree(b), 'branches must be trees'

    # concatenates two lists into one
    # print([label] + list(branches))
    return [label] + list(branches)


def print_tree(t, indent=0):
    # so it's ok to pass default arguments into functions straight away

    # if is_leaf(t):
    #     return f'{indent*" "}{label(t)}\n'
    #
    # total_s = f'{indent*" "}{label(t)}\n'
    # for b in branches(t):
    #     total_s += print_tree(b, indent+1)
    # return total_s

    # or a similar solution that prints directly (no need for \n)
    if is_leaf(t):
        print(" "*indent + str(label(t)))
    else:
        print(" "*indent + str(label(t)))
        for b in branches(t):
            print_tree(b, indent+1)


t = tree(3, [tree(1),
             tree(2, [tree(1),
                      tree(1)])])

t1 = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])
t2 = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(2)]), tree(6)])

# ==============================================================================
# exercises start


def make_adder_inc(n):

    counter = -1

    def adder_inc(x):
        nonlocal counter
        counter += 1
        return n + x + counter

    return adder_inc


adder1 = make_adder_inc(5)
# print(adder1(2))
# print(adder1(2))
# print(adder1(10))
# print([adder1(x) for x in [1, 2, 3]])


def make_fib():
    """Returns a function that returns the next fib number every time it's called."""

    # option 1 - using n
    # n = 0
    # def fib():
    #     # NOTE: recursive won't work here because we're not passing n as argument
    #     nonlocal n
    #     i = 0
    #     curr, next = 0, 1
    #     while i < n:
    #         curr, next = next, curr+next
    #         i += 1
    #     n += 1
    #     return curr

    # option 2, using curr, next as nonlocals to begin with - much simpler!
    curr, next = 0, 1

    def fib():
        nonlocal curr, next
        curr, next = next, curr+next
        return curr

    return fib


fib = make_fib()
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())


def scale(it, multiplier):
    """Yields the iterator scaled by multiplier."""

    # option 1 - using yield
    # for i in it:
    #     yield i*multiplier

    # option 2 - using yield from
    yield from map(lambda i: i*multiplier, it)


m = scale([1, 5, 2], 5)
# print(type(m))
# print(list(m))


def hailstone(n):
    """Yields the hailstone sequence.
    Reminder:
    1. Pick n
    2. If n is even, dividy it by 2
    3. If n is odd, multiply it by 3 and add 1
    4. Contnue until n is 1
    """

    yield n
    if n > 1:
        if n % 2 == 0:
            yield from hailstone(n//2)
        else:
            yield from hailstone(n*3+1)


def recursively_yield(n):
    """Recursively yields numbers from n downwards until n == 0."""

    yield n
    if n > 0:
        yield from recursively_yield(n-1)


for num in recursively_yield(10):
    print(num)


print("-------------------- Guerrilla 02 --------------------")

"""
1.1
lists, dicts = can change values after defined

1.2
tuple, functions, ints, floats = ALL immutable

1.3
the second part will because keys in dictionaries need to be immutable

1.4


"""
a = [1, [2, 3], 4]
c = a[1]
a.append(c)
c[0] = "asfasdf"
print(a)

a.extend(c)
print(a)

c[1] = 9
print(a)


def is_min_heap(t):
    """Checks if a tree is a min heap. Long version."""
    flag = True

    def check_heap(t):
        nonlocal flag
        if is_leaf(t):
            return label(t)
        else:
            for b in branches(t):
                if label(t) > label(b):
                    flag = False
                check_heap(b)

    check_heap(t)
    return flag


def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            # very interesting way to pass down False from subbranches - if any of them evals to False, not False becomes True, which is a condition here and so we return False
            return False


# print(t)
# print(is_min_heap(t1))
# print(is_min_heap(t2))


# def largest_prod_path(t):
#
#     bs = []
#
#     def traverser(t):
#         nonlocal bs
#
#         if is_leaf(t):
#             return label(t)
#         else:
#             max_ = max([traverser(b) for b in branches(t)])
#
#             for b in branches(t):
#                 if traverser(b) == max_:
#                     bs.append(label(b))
#                     return label(b)
#
#     traverser(t)
#     return bs


def largest_prod_path(t):
    # ok first of all I didn't read the exercise properly - they wanted largest product, not a list of nodes
    # sceondly - fuck the solution was on the tip of my tongue. Each time take the max. Each time multiply existing by max. Gives you total max. That's it.
    if not t:
        return 0
    elif is_leaf(t):
        return label(t)
    else:
        paths = [largest_prod_path(b) for b in branches(t)]
        return label(t) * max(paths)


# print_tree(t1)
# print(largest_prod_path(t1))


def max_tree(t):
    """Takes a tree and returns one with exact same struct but each node being max of branches / itself."""
    if is_leaf(t):
        return t
    else:
        # my version
        # all_labels = [label(t)] + [label(max_tree(b)) for b in branches(t)]
        # return tree(max(all_labels), [max_tree(b) for b in branches(t)])

        # their version
        new_branches = [max_tree(b) for b in branches(t)]
        new_label = max([label(t)] + [label(b) for b in new_branches])
        return tree(new_label, new_branches)


print_tree(t1)
print('-------')
# print_tree(max_tree(t1))
# print_tree(max_tree(tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])))


def level_order(t):
    # ok here's a shitty solution

    list_of_labels = [label(t)]

    def traverser(t):

        nonlocal list_of_labels

        if is_leaf(t):
            # list_of_labels.append(label(t))
            return label(t)
        else:
            # print(
            #     f'currently label is {label(t)} and branches are {[label(b) for b in branches(t)]}')
            list_of_labels.extend([label(b) for b in branches(t)])
            for b in branches(t):
                traverser(b)

    traverser(t)
    return list_of_labels


def better_level_order(t):
    # if we've reached the bottom - return empty list. our base case.
    if not t:
        return []

    # some arbitrary variables that will help us along the way
    current_level, next_level = [label(t)], [t]

    # while there still exists a next level and it's not empty
    while next_level:
        find_next = []
        for b in next_level:
            find_next.extend(branches(b))
        next_level = find_next
        current_level.extend([label(t) for t in next_level])
    return current_level

    # what's similar to my solution is that they also used an overall list to store labels, and intiialized it with label(t)
    # what's different is they used iteration while I used recursion. That's also why I had to define another function inside that function
    # I actually think my solution is better


# print(level_order(t1))

def all_paths(t):

    # close but not really
    # if is_leaf(t):
    #     return [label(t)]
    # else:
    #     paths = []
    #
    #     for b in branches(t):
    #         path = [label(t)] + all_paths(b)
    #         paths.append(path)
    #
    #     return paths

    # close but again not quite
    # paths = []
    # def branch_appender(t, lst):
    #     if is_leaf(t):
    #         lst.append(label(t))
    #     else:
    #         for b in branches(t):
    #             branch_appender(b, lst)
    #
    # for b in branches(t):
    #     new_path = [label(t), label(b)]
    #     branch_appender(b, new_path)
    #     paths.append(new_path)
    #
    # return paths

    if is_leaf(t):
        return [[label(t)]]
    else:
        # each of these "total" lists will become an array
        total = []
        for b in branches(t):
            # here we do the leap of faith - we trust that all_paths returns [[x,x], [y,y]] for some branch b
            for path in all_paths(b):
                # if it indeed does then we take the total and append label(t) plus each of those
                # if you're wondering where label of b is - it's in the "path" variable, the same way that path for t starts with t
                total.append([label(t)] + path)
        return total


print(all_paths(t1))

x = 3


def try_(f): return f(x)


# NOTE: when we write variable = lambda x:x we're assigning a function object to it, not the result of calling the function - it's equivalent to writing the def statement.
# print(try_)
spiderman = "peter parker"


def spider(man):
    def myster(io):
        nonlocal man
        man = spiderman  # fetches spiderman from global scope, which is "peter parker"
        # nonlocal man is now "peter parker"
        # io = the gratest super hero
        def spider(stark): return stark(man) + ' ' + io
        return spider  # returns a function object
    return myster  # returns a function object


truth = spider('quentin is')('the greatest superhero')(lambda x: x)
# print(truth)


def make_max_finder():

    LoL = []

    def find_max(L):
        nonlocal LoL
        LoL.extend(L)
        return max(LoL)

    return find_max


m = make_max_finder()
# print(m([5, 6, 7]))
# print(m([1, 2, 3]))
# print(m([9]))

x = 5


def f(x):
    def g(s):
        def h(h):
            nonlocal x
            x = x + h  # takes x from above, which is 7 + h which is 9
            return x  # returns 16, nonlocal x also 16 now
        nonlocal x  # 16
        x = x + x  # 32
        return h  # returns h the function

    print(x)  # prints 28
    return g


# t = f(7)  # sets x to 7, creates the other functions, prints 7, returns g with 7 baked in
# t2 = t(8)  # sets nonlocal x to 14, returns h
# t3 = t2(9)  # 14 + 9 = 23
# print(t3)

print("-------------------- GENERATORS --------------------")


def infinity2(start):
    while True:
        start += 1
        yield start


x = infinity2(2)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(infinity2(2)))


def generate_constant(x):

    while True:
        yield x


area = generate_constant(51)
# print(next(area))
# print(next(area))
# print(next(area))
# print(next(area))


def black_hole(seq, trap):
    for i in seq:
        if i == trap:
            yield from generate_constant(trap)
        else:
            yield i


# trapped = black_hole([1, 2, 3], 2)
# print([next(trapped) for _ in range(10)])
# print(list(black_hole(range(5), 7)))
#

def weird_gen(x):
    if x % 2 == 0:
        yield x


wg = weird_gen(2)
# print(next(wg))
# print(next(weird_gen(2)))


def wtf(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


w = wtf(10)
# print([next(w) for _ in range(5)])


def greeter(x):
    while x % 2 != 0:
        print('hi')
        yield x
        # interesting behavior - this will only be run when we call the next next() after the above yield
        print('bye')


# gen = greeter(5)
# g = next(gen)
# g = (g, next(gen))
# print(g)


def gen_inf(L):
    # normal version
    # while True:
    #     yield from L

    # itertools version
    yield from itertools.cycle(L)


# L = [3, 4, 5]
# gen = gen_inf(L)
# for _ in range(10):
#     print(next(gen))


def filter(iterable, fn):
    """Only yields elements for which fn returns true."""

    # generator approach
    # for i in iterable:
    #     if fn(i):
    #         yield i

    # itertools approach, a little bit complex compared to the above
    yield from itertools.compress(iterable, [fn(i) for i in iterable])


# L = range(55)
# gen = filter(L, lambda x: x % 2 == 0)
# for _ in range(10):
#     print(next(gen))


def make_digit_getter(n):

    total = 0

    # YIELD + NONLOCAL IN ONE FUNC FEEL REDUNDANT
    # def digit_yielder():
    #     nonlocal n, total
    #
    #     # keep going until we're out of digits
    #     while n > 0:
    #         last_digit, n = n % 10, n//10
    #         total += last_digit
    #         yield last_digit
    #
    #     # we need a second infinite while loop because we want to return total for any number of calls after the generator exhausts above
    #     while True:
    #         yield total

    # SIMPLER
    def digit_yielder():
        nonlocal n, total
        if n == 0:
            return total
        last_digit, n = n % 10, n//10
        total += last_digit
        return last_digit

    return digit_yielder


# m = make_digit_getter(12345)() #NOTE the little brackets at the end, if you're using yield you have to do this
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

m = make_digit_getter(12345)
print(m())
print(m())
print(m())
print(m())
print(m())
print(m())
print(m())
