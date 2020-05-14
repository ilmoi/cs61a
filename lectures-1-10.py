print("-------------------- L4 - ENV --------------------")


def make_adder(n):
    # n saved here
    def adder(k):
        return n+k
    return adder


three = make_adder(3)
seven = three(4)
print(seven)

# interesting way to call functions, didn't know you could do that
seven_again = make_adder(3)(4)
print(seven_again)

print("-------------------- L5 - HIGH ORDER FUNCS --------------------")


def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total+k, k+1
    return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= 5:
        total, k = total+k**3, k+1
    return total


def gen_sum(n, pow_):
    """General version of the two above"""
    total, k = 0, 1
    while k <= 5:
        total, k = total+pow_(k), k+1
    return total


def identity(k): return k


def cube(k): return k**3


def print_sums(n):
    print(n)  # desired output

    def next_sum(k):
        return print_sums(n+k)
    return next_sum


print(sum_naturals(5))
print(sum_cubes(5))
print(gen_sum(5, cube))

# note how because it's a recursive function we can keep adding arguments to the right and it will still work!
print_sums(1)(2)(4)(10)

print("-------------------- L7/8 - REC --------------------")


def sum_digits(n):
    """Calculates the sum of all digits of n"""

    # painful implementation, going through a list
    # n = [i for i in str(n)]
    # if len(n) == 1:
    #     return int(n[0])
    # else:
    #     p = int(n.pop())
    #     return sum_digits(int(''.join(n))) + p

    # a cleaner implementation using strings
    # n = str(n)
    # if len(n) == 1:
    #     return int(n)
    # else:
    #     return sum_digits(int(n[:-1])) + int(n[-1])

    # lets try one more using pure ints
    if n < 10:
        return n
    else:
        # floor, rem = divmod(n, 10)
        # return sum_digits(floor) + rem

        # or the alternative, using floor division and modulo
        return sum_digits(n//10) + n % 10


def find_n(n):
    # when writing recursive functions we ALWAYS want to put the BASE case FIRST
    if n == 1:
        print("I'm the first one!")
        return 1
    else:
        print('gonna ask the person in front of me and add one')
        return find_n(n-1)+1


def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        # note no return statement otherwise the bottom print statement gets cut off and never executes
        cascade(n//10)
        print(n)


def fibs(n):
    """Returns nth fib. Eg 7 should return 13."""
    # base case first
    if n <= 1:
        return n
    else:
        return fibs(n-2) + fibs(n-1)


def iter_fibs(n):
    i = 0
    curr, next = 0, 1
    while i < n:
        curr, next = next, curr+next
        i += 1
    return curr


def count_part(n, m):
    """counts number of possible ways to give out N (>0) pieces of chocolate
    to any number of people, given none can have more than M (>0) pieces to themselves.

    Order doesn't matter.

    eg count_part(6,4) should re turn 9.
    """

    if n < 0:
        return 0  # failed
    elif n == 0:
        return 1  # succeeded
    elif m == 0:
        return 0  # failed
    else:
        # where we DO use m, and where we DON'T use m
        return count_part(n-m, m) + count_part(n, m-1)


# n = find_n(45)
# print(n)
print(sum_digits(20178))
cascade(486)
print(fibs(7))
print(iter_fibs(7))
print(count_part(6, 4))


print("-------------------- L10 - MORE ITERABLE STUFF --------------------")

# you can use sum to concat lists, you just need to make sure to pass an empty list at the end
print(sum([[1, 2, 3], [1]], []))

# you can use min max with a key
print(max([1, 2, -3]))
print(max([1, 2, -3], key=abs))

# you can use min max with a string
print(max(['a', 'b', 'c']))

# bool converts to T/F
print(bool(0))  # false
print(bool([]))  # false
print(bool({}))  # false
print(bool(""))  # false
print(bool(" "))  # note this is true, since not empty

# all applies that to a list
print(all([0, 1, 1]))
print(all([1, 1, 1]))

# any looks for at least one true
print(any([1, 0, 0]))

# we can use list comprehension to get true / false filters
print([x > 5 for x in range(7)])

print("-------------------- TREES --------------------")


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


t = tree(3, [tree(1),
             tree(2, [tree(1),
                      tree(1)])])

l = tree(1)
print(is_leaf(t))  # false coz it's actually a tree not a list
print(is_leaf(l))
print(is_tree(t))  # true
print(is_tree(l))  # true coz leaf is a small tree, but a tree is not a leaf

# NOTE: in order not to break the abstraction barrier, we should never index into a tree directly (in theory we don't know they're implemented as trees in the background)
print(t[1])  # BAD
print(branches(t))  # GOOD - USING THE SELECTOR


print("-------------------- FUNCTS ON TOP OF TREES --------------------")


def count_nodes_in_tree(t):

    # NOTE: in this particular case base case is OPTIONAL
    # reason for this: if branches below is an empty list we still return 1
    # this is NOT TYPICAL and should not be relied upon

    # if is_leaf(t):
    #     return 1

    # normal list view
    # total = 1
    # for b in branches(t):
    #     total += count_nodes_in_tree(b)
    # return total

    # shorter, list comprehension view
    return 1 + sum([count_nodes_in_tree(b) for b in branches(t)])


print(count_nodes_in_tree(t))


def gather_all_leaves(t):

    if is_leaf(t):
        return [label(t)]

    # full view
    # labels = []
    # for b in branches(t):
    #     labels += gather_all_leaves(b)
    # return labels

    # shorter list view
    return sum([gather_all_leaves(b) for b in branches(t)], [])


print(gather_all_leaves(t))


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


print_tree(t)


def double_the_tree(t):

    # another case where we can skip the basecase
    # if is_leaf(t):
    #     return tree(label(t)*2)

    new_bs = []
    for b in branches(t):
        new_bs.append(double_the_tree(b))
    return tree(label(t)*2, new_bs)


l = tree(1)
ll = double_the_tree(l)
print(ll)

t = tree(3, [tree(1),
             tree(2, [tree(1),
                      tree(1)])])

tt = double_the_tree(t)
print(t)
print(tt)


def fib_tree(n):
    """
    Returns a fib tree with root label fib(n)
    """

    if n <= 1:
        return tree(n)
    else:
        left = fib_tree(n-1)
        right = fib_tree(n-2)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


# print_tree(fib_tree(5))
