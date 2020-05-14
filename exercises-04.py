import copy
import itertools


def skip_add(n):
    """Takes an arg n, and computers the sum of every other integer between 0 and n."""

    if n <= 1:
        return n
    else:
        return n + skip_add(n-2)


# print(skip_add(10))


def paths(m, n):
    """Returns the number of paths from bottom left to top right corner in MxN grid."""

    # def helper(m_left, n_left):
    #     # m_left and n_left signify how many squares there still are in each direction
    #     if m_left == 1 and n_left == 1:
    #         return 1
    #     elif m_left == 1:
    #         return helper(m_left, n_left-1)
    #     elif n_left == 1:
    #         return helper(m_left-1, n_left)
    #     else:
    #         return helper(m_left-1, n_left) + helper(m_left, n_left-1)

    def helper(m_left, n_left):
        # an even shorter solution - we don't actually need to "crawl" all the way to the end
        if m_left == 1 or n_left == 1:
            return 1
        else:
            return helper(m_left-1, n_left) + helper(m_left, n_left-1)

    return helper(m, n)


# print(paths(5, 7))


def max_subseq(n, l):
    """Return maximum sequence of length l built from n."""

    # just for jokes here's the itertools approach, which kinda works
    # total = 0
    # for i in range(l+1):
    #     combos = list(itertools.combinations([i for i in str(n)], i))
    #     print(combos)
    #     total += len(combos)
    #
    # return total

    if n == 0 or l == 0:
        return 0

    # my hunch about taking or not taking a certain digit was correct
    with_last = max_subseq(n//10, l-1)*10 + n % 10
    without_last = max_subseq(n//10, l)
    # my hunch about max was also correct
    return max(with_last, without_last)

    # what I mainly missed was that you should reduce INSIDE the max_subseq() and increment OUTSIDE.


# print(max_subseq(20125, 3))


def count_stair_ways(n):
    """Counts number of ways you could climb a bunch of stairs, taking either 1 or 2 steps"""

    if n == 0:
        return 1
    # this could also be if n == 1: return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)


# print(count_stair_ways(10))

def count_k(n, k):
    """Version of the stairs problem but this time we can take up to k steps included."""

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        # their option, which I think is too heavy
        # total = 0
        # i = 1
        # while i <= k:
        #     total += count_k(n-i, k)
        #     i += 1
        # return total

        # my option
        return sum([count_k(n-i, k) for i in range(1, k+1)])


# print(count_k(10, 3))


def even_weighted(s):
    """Takes a list, returns even indexed elems multiplied by index."""

    # return [i*e for i, e in enumerate(s) if i % 2 == 0]
    # alternative
    return [i*s[i] for i in range(len(s)) if i % 2 == 0]


# print(even_weighted([1, 2, 3, 4, 5, 6]))


def max_product(s):

    if len(s) == 1:
        print(f'only one option {s[0]}')
        return s[0]
    elif len(s) == 0:
        print('nothing to take!')
        return 1
    else:
        print(f"list is {s}, should we take {s[-1]}?")
        # should have used max! not plus!
        return max(max_product(s[:-2]) * s[-1], max_product(s[:-1]))


# print(max_product([10, 3, 1, 9, 2]))


def map_mut(f, L):
    # the below returns a new list, doesn't mutate the existing one in place
    # L = [f(i) for i in L]
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, 2, 3, 4, 5]
map_mut(lambda x: x**2, L)
print(L)

# 1.4
L2 = L[:]  # copy
L2 = L  # copy

# NOTE when we copy a list, if it has ANOTHER list INSIDE of it - we only copy POINTERS
# proof:


def manual_deep_copy(L):
    new_L = []
    for i in L:
        if type(i) == list:
            new_L.append(manual_deep_copy(i))
        else:
            new_L.append(i)
    return new_L


L1 = [1, 2, [3, 4]]
L2 = L1
L3 = copy.deepcopy(L1)
L4 = manual_deep_copy(L1)
print(L1, L2, L3, L4)
L2[0] = 'abc'
print(L1, L2, L3, L4)
L2[2][1] = 'def'
print(L1, L2, L3, L4)

# this gives rise to the concept of shallow and deep copy
# shallow copy = see L2 above
# deep copy = see L3 above
# a manual way to write a deepcopy function = see L4 above


def cascade2(n):
    print(n)
    if n >= 10:
        cascade2(n//10)
        print(n)


cascade2(158)


def merge(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        if s1[-1] > s2[-1]:
            return merge(s1[:-1], s2) + [s1[-1]]
        else:
            return merge(s1, s2[:-1]) + [s2[-1]]


print(merge([1, 3], [2, 4]))


def mario_number(level):
    """Returns the # of ways mario can traverse a piranha path."""

    if len(level) == 0 or len(level) == 1 or len(level) == 2:
        return 1
    elif level[0] == "P":
        raise Exception('mario loses! impossible!!')
    else:
        if level[1] == "P":
            return mario_number(level[2:])
        elif level[2] == "P":
            return mario_number(level[1:])
        else:
            return mario_number(level[1:]) + mario_number(level[2:])


print(mario_number('---P----P-P---P--P-P----P-----P-'))
