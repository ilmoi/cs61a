this_file = __file__

# Mobiles

# ==============================================================================
# Helper code 1 - MOBILES


def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


# ==============================================================================
# Helper code 2 - ARMS


def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


# ==============================================================================
# Q1 = planet


def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet', size]


def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]


def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'


def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


# ==============================================================================
# Q2 = balanced


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return True

    end_left = end(left(m))
    end_right = end(right(m))
    torque_left = length(left(m)) * total_weight(end_left)
    torque_right = length(right(m)) * total_weight(end_right)

    return balanced(end_left) and balanced(end_right) and (torque_left == torque_right)


# a1 = arm(10, planet(30))
# a2 = arm(10, planet(20))
# m1 = mobile(a1, a2)
# a3 = arm(6, m1)
# # 300 vs 6*  total weight which is 50
# m2 = mobile(a1, a3)
# print(a1)
# print(a2)
# print(m1)
# print(m2)
# print('-----------')
# print(balanced(m1))

# ==============================================================================
# Q3 = totals


def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    "*** YOUR CODE HERE ***"

    weight = total_weight(m)
    if is_planet(m):
        return tree(weight, [])
    else:
        return tree(weight, [totals_tree(end(left(m))), totals_tree(end(right(m)))])


def replace_leaf(t, old, replacement):
    """Returns a new tree where every leaf value equal to old has
    been replaced with replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) == old:
            return tree(replacement)
        else:
            return tree(label(t))

    return tree(label(t), [replace_leaf(b, old, replacement) for b in branches(t)])


# t = tree(1, [tree(2), tree(4, [tree(2), tree(3)])])
# new_t = replace_leaf(t)
# print_tree(new_t)

# def old_make_withdraw(balance):
#
#     def withdraw(amount):
#         nonlocal balance
#         print(f'left {balance-amount}')
#         return balance-amount
#
#     return withdraw


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"

    pwds = []

    def withdraw(amount, pwd):
        nonlocal balance
        # nonlocal pwds #NOTE does NOT need to be non-local we're not mutating it we're just reassining it
        # nonlocal password # don't need this either because you're NOT MUTATING IT at any point

        if len(pwds) == 3:
            return f"Your account is locked. Attempts: {str(pwds)}"

        if pwd != password:
            pwds.append(pwd)
            # print(f'state of wrong pwds is {pwds}')
            return 'Incorrect password'

        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance

    return withdraw


# w = make_withdraw(1000, 'hax0r')
# print(w(100, 'hax0rr'))
# print(w(100, 'hax0rr'))
# print(w(100, 'hax0rr'))
# print(w(100, 'hax0rr'))


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    # new accounts can use new pws and old pws, but old accounts can only use odl pws
    # all accounts share a single list of pws, which we'll define here
    # if one account is locked - all accounts are locked

    # the first argument is an ALREADY FORMED withdraw from the function above - so it already has a list, a pw, and all req error-making capabilities
    # so this function is really a wrapper - it shouldn't be "thinking" on its own

    test = withdraw(0, old_pass)
    if type(test) == str:
        return test  # passing on and closing the function

    def withdraw_joint(amount, pwd):
        if pwd == new_pass:
            pwd = old_pass
        return withdraw(amount, pwd)

    return withdraw_joint


# w = make_withdrawal(100, 'hax0r')
# print(w(25, 'hax0r'))
# print(w(25, 'secret'))
# print(make_joint(w, 'my', 'secret'))
# j = make_joint(w, 'hax0r', 'secret')
# print(j(25, 'secret'))
# print(j(25, 'hax0r'))
# print(j(100, 'secret'))
#
# j2 = make_joint(j, 'secret', 'code')
# print(j2(5, 'code'))
# print(j2(5, 'secret'))
# print(j2(5, 'hax0r'))
#
# print(j2(25, 'password'))
# print(j2(5, 'secret'))

## Tree Methods ##


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

###################
# Extra Questions #
###################


def interval(a, b):
    """Construct an interval from a to b."""
    assert a <= b
    return [a, b]


def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    assert type(x) == list and len(x) == 2
    return x[0]


def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    assert type(x) == list and len(x) == 2
    return x[1]


def str_interval(x):
    """Return a string representation of interval x.
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# i = interval(-1, 2)
# j = interval(4, 8)
# z = mul_interval(i, j)
# print(str_interval(z))
# print(str_interval(mul_interval(interval(-1, 2), interval(4, 8))))
# print(str_interval(add_interval(interval(-1, 2), interval(4, 8))))


def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)


# print(str_interval(sub_interval(interval(-1, 2), interval(4, 8))))


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert not (lower_bound(y) <= 0 <= upper_bound(y))
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))


def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


def multiple_references_explanation():
    return """The multiple reference problem..."""


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    l = lower_bound(x)
    u = upper_bound(x)
    calc1 = a*l*l + b*l + c
    calc2 = a*u*u + b*l + c
    return interval(min(calc1, calc2), max(calc1, calc2))


print(str_interval(quadratic(interval(0, 2), -2, 3, -1)))
