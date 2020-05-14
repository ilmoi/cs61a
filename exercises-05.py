import hw04


def label(tree):
    """Abstract datatype tree LABEL SELECTOR"""
    return tree[0]


def branches(tree):
    """Abstract datatype tree BRANCHES SELECTOR"""
    return tree[1:]  # IMPORTANT: [1:] not [1]. In this way we're saying 0th item onwards, not 1st item - and we need that for leaves


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

# ==============================================================================


def height(t):
    """Returns the height of the tree == the len of longest branch."""

    # if is_leaf(t):
    #     return 0
    # else:
    #     heights = []
    #     for b in branches(t):
    #         heights.append(height(b))
    #     return 1 + max(heights)

    # write in one line
    return 1 + max([-1]+[height(b) for b in branches(t)])


print(height(t))
t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])


def find_path(t, x):
    """My (long) version of finding a path to some leaf."""
    # two parts
    # part 1 - rebuild the tree

    def get_tree(t, x):
        if is_leaf(t):
            if label(t) == x:
                return label(t)
        else:
            paths = []
            paths.append(label(t))
            for b in branches(t):
                # FUCK ME - THE NUMBER OF TIMES I MISTAKENLY WROTE T NOT B
                paths.append(get_tree(b, x))
            return paths

    # part 2 - flatten and prune the array

    tr = get_tree(t, x)
    final = []
    flag = True
    while flag:
        flag = False
        for t in tr:
            if type(t) == int:
                final.append(t)
            elif type(t) == list:
                tr = t
                flag = True

    return final


# print(find_path(t, 5))

def find_path(t, x):
    if label(t) == x:
        # there's only one return statement in the whole thing and it returns the label
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        # because there's only one return label - here we check if it indeed was returned
        if path:
            return [label(t)] + path  # if it did, we concat the path


# print(find_path(t, 5))

"""
ADT t = tree(1, [tree(2), tree(3)]).

1. label(t)
- 1
- ok
2. t[0]
- 1
- not ok, the above expression should be used to get the label
3. label(branches(t)[0])
- 2
- ok - we're not violating the barrier coz we know for a fact that branches is a list. we don't go into the implementation of individual branches
4. label(branches(t))
- error
5. is leaf(t[1:][1])
- returns the second branch which is tree(3)
- not ok, we're accessing branches direclty rather than using a getter
6. [label(b) for b in branches(t)]
- labels of all first level branches
- ok
7. Challenge: branches(tree(2, tree(t, [])))[0]

1 label = tree(1, [tree(2), tree(3)]), but label is useless so really we have
1 tree(t, [])
2 tree(2, tree(t, []))
3 tree(t, [])
returns t = tree(1, [tree(2), tree(3)])

yes violates when we access t


# ==============================================================================
>>> lst1 = [1, 2, 3]

>>> lst2 = lst1

>>> lst1 is lst2
true... didn't know that

>>> lst2.extend([5, 6])
nothing but lst2 becomes [1,2,3,5,6]

>>> lst1[4]
6

>>> lst1.append([-1, 0, 1])
nothing but lst1 is [1, 2, 3, 5, 6, [-1, 0, 1]]

>>> -1 in lst1
false

>>> lst2[5]
[-1,0,1]

>>> lst3 = lst2[:]
nothing but lst3 becomes a copy of lst2

>>> lst3.insert(3, lst2.pop(3))
lst2 is [1, 2, 3, 5, 6, [-1, 0, 1]]
pops 5
lst2 becomes [1, 2, 3, 6, [-1, 0, 1]]
lst3 is [1, 2, 3, 5, 6, [-1, 0, 1]]
lst3 becomes [1, 2, 3, 5, 5, 6, [-1, 0, 1]]

>>> len(lst1)
5

>>> lst1[4] is lst3[6]
yes!!! because we made a shallow copy!!

>>> lst3[lst2[4][1]]
1

>>> lst1[:3] is lst2[:3]
no because diff objects

>>> lst1[:3] == lst2[:3]
yes

>>> x = (1, 2, [4, 5, 6])

>>> x[2] = [3, 5, 6]
error since x is a tuple

>>> x
the same

>>> x[2][0] = 3
ok

>>> x
x = (1, 2, [3, 5, 6])

"""
# x = (1, 2, [4, 5, 6])
# print(x)
# x[2][0] = 1
# print(x)

# lst1 = [1, 2, 3]
# lst2 = lst1
# print(lst1 is lst2)
# lst2.extend([5, 6])
# lst1.append([-1, 0, 1])
# lst3 = lst2[:]
# lst3.insert(3, lst2.pop(3))
# print(len(lst1))
# print(lst1[4] is lst3[6])
# print(lst3[lst2[4][1]])
# print(lst1[:3] is lst2[:3])
#
# print(f'lst1 is {lst1}')
# print(f'lst2 is {lst2}')
# print(f'lst3 is {lst3}')


def add_this_many(x, el, lst):
    [lst.append(el) for _ in range(x)]


lst = [1, 2, 4, 2, 1]
add_this_many(5, 5, lst)
print(lst)


def group_by(s, fn):
    """Takes in a list s and groups according to output of function f(n). Returns as dics."""

    fns = [fn(i) for i in s]
    dict = {}

    for i in range(len(fns)):
        dict[fns[i]] = dict.get(fns[i], [])
        dict[fns[i]].append(s[i])

    return dict


# print(group_by([12, 23, 14, 45], lambda p: p // 10))


def partition_options(total, biggest):
    if total == 0:
        return [[]]
    elif total < 0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total-biggest, biggest)
        without_biggest = partition_options(total, biggest-1)
        with_biggest = [[biggest] + elem for elem in with_biggest]
        return with_biggest + without_biggest


# print(partition_options(2, 2))


def min_elements(T, lst):
    """Returns the minimum number of elements from the list that need to be summed to add up to T."""
    # assume the list is ordered from biggest to smallest

    # def helper(total, lst):
    #     # print(f'total is {total}, lst is {lst}')
    #     if total == 0:
    #         # print('case 1')
    #         return 1
    #     elif total < 0:
    #         # print('case 2')
    #         return 0
    #     elif not lst or lst == []:
    #         # print('case 3')
    #         return 0
    #     else:
    #         with_largest = 1 + helper(total - max(lst), lst)
    #         without_largest = 1 + helper(total, lst[1:])
    #         return min(with_largest, without_largest)
    #
    # return helper(T, lst)

    if T == 0:
        return 0
    # give me the minimum of a list of all Is
    # as long as i < T (if it's larger we go into negative territory and overshoot)
    return min([1 + min_elements(T-i, lst) for i in lst if T-i >= 0])


print(min_elements(10, [4, 2, 1]))
print(min_elements(12, [9, 4, 1]))
