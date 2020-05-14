def multiply(m, n):
    """Takes two inputs and recursively returns product."""
    if n == 1:
        return m
    else:
        return multiply(m, n-1) + m


# print(multiply(5, 3))


def countdown(n):
    """Takes an integer n and prints out a countdown from n to 1."""
    if n == 1:
        return
    else:
        print(n-1)
        return countdown(n-1)


# countdown(10)


def hailstone(n, counter=0):
    """Print the hailstone sequence starting at n + returns # of elems"""
    # hailstone seq = if n is even, div by 2, else mult by 3 and add 1
    # NOT A VERY ELEGANT SOLUTION, NEED TO KEEP TRACK OF COUNTER MANUALLY

    print(n)
    counter += 1
    if n == 1:
        return counter  # if put print here, then we have two of those
    else:
        if n % 2 == 0:
            return hailstone(n//2, counter)
        else:
            return hailstone(n*3+1, counter)


def hailstone_better(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)  # we're buildilng the counter into return
    else:
        return 1 + hailstone(n*3+1)


# print(hailstone_better(10))


def is_prime(n, k=2):
    """Resturns True if number is prime, else False."""

    if n == 1:
        return False
    elif n % k == 0:
        return False
    elif k == n-1:
        return True
    else:
        return is_prime(n, k=k+1)


# print(is_prime(13))


def merge(n1, n2):
    """Takes two numbers with digits in decr. order and merges them into a single number with digits in decr. order"""

    # eg 31 and 42 = 4321

    # at any one point you want to pick the number with the smallest right digit

    print(f'comparing {n1} and {n2}')

    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        print(f'comparing(2) {n1%10} and {n2%10}')
        if n1 % 10 <= n2 % 10:
            # one way to do this is using strings
            # return str(merge(n1//10, n2)) + str(n1 % 10)
            # but a better way is to just multiply by 10
            return merge(n1//10, n2) * 10 + n1 % 10
        else:
            return merge(n1, n2//10) * 10 + n2 % 10


# print(merge(31, 43))
def make_func_repeater(f, x):
    """This function performs function f on x x times"""

    def repeat(x):
        if x == 1:
            return x
        else:
            # you end up having a f(f(f(f(x)))) type construct
            return f(repeat(x-1))

    return repeat


p = make_func_repeater(lambda x: x+1, 1)
# print(p(6))


def num_sevens(x):
    "returns the number of times 7 appears in digit x"

    if x == 0:
        return 0
    elif x % 10 == 7:
        return 1 + num_sevens(x//10)
    else:
        return num_sevens(x//10)


# print(num_sevens(74473))

# ==============================================================================
# the ugly way
def switch(k):
    if num_sevens(k) > 0:
        return True
    elif k % 7 == 0:
        return True
    else:
        return False


def better_switch(k, funcs):
    # this type of switch would return the relevant function not just true or false
    if num_sevens(k) > 0 or k % 7 == 0:
        return [funcs[1], funcs[0]]
    else:
        return funcs


print(switch(17))


def incr(i):
    return i + 1


def decr(i):
    return i - 1


def ugly_pingpong(n, k=1, j=1, func=incr):
    """Implements the ping pong sequence."""

    print(f'in this round n is {n}, k is {k}, j is {j}')

    # terminal condition
    # their version: if i == n: return result
    if k == n:
        return j

    else:
        if switch(k):
            if func == incr:
                func = decr
            else:
                func = incr

        return ugly_pingpong(n, k=k+1, j=func(j), func=func)


# print(ugly_pingpong(29))

# ==============================================================================
# their way


def pingpong(n):
    """Implements the ping pong sequence."""

    def helper(result, i, step):
        # nice - because they're defining a function inside a function two things happen:
        # 1)n stays constant without having to pass it as n=n, because it's defined in the scope outside the function
        # 2)we go from 1 variable (n) to 3 variables (result, i, step) - while the external function still only has one
        # this is the biggest thing I missed. otherwise my solution was correct.

        # I was right that you need some sort of internal counter going from 1 to i == n
        # and that you need a separate result variable
        if i == n:
            return result
        elif i % 7 == 0 or num_sevens(i) > 0:
            # I was right in that you need to somehow pass down the function, as it needs to be re-used by the next steps before next switch
            # very elegant way to do a "switch" - whenever it's switch time you just pass the negative value in
            return helper(result-step, i+1, -step)
        else:
            return helper(result+step, i+1, step)

    return helper(result=1, i=1, step=1)


# print(pingpong(29))

# ==============================================================================
# iterative version


def change_dir(step, i):
    if i % 7 == 0 or num_sevens(i) > 0:
        return -step
    else:
        return step


print(change_dir(1, 7))


def iter_pong(n):

    # same story as before, we need to track the index and the result
    index = 1
    result = 1
    step = 1
    while index < n:
        print(f'index is {index}, result is {result}, step is {step}')
        # yes need to do on sepa line, so that you can pass it down from there
        step = change_dir(step, index)
        result += step
        index += 1

    return result


# print(iter_pong(29))

print("-------------------- Q3 MAKE CHANGE --------------------")
# machine does powers of 2: 0,1,2,3... = 1 2 4 8 etc


def highest_power_of_two(n):
    res = 0
    for i in range(n):
        if 2**i <= n:
            res = i
    return res


def count_change(n):
    """Returns the total number of ways you can make change with machine coins"""

    power = highest_power_of_two(n)
    total = n

    def helper(total, power):
        print(f'total is {total}, power is {power}')

        if total < 0:
            print(f'oops overshot total to {total}')
            return 0
        elif total == 0:
            print(f'BINGO')
            return 1
        elif 2**power < 1:
            print(f'oops overshot power to {power}')
            return 0
        else:
            return helper(total - 2**power, power) + helper(total, power-1)

    return helper(total, power)


# print(count_change(10))
# nice it works!


def their_count_change(total):
    def constrained_count(total, smallest_coin):
        # interesting so they managed to start with smallest coin
        if total == 0:
            return 1
        if smallest_coin > total:
            return 0
        with_coin = constrained_count(total-smallest_coin, smallest_coin)
        without_coin = constrained_count(total, smallest_coin*2)
        return without_coin + with_coin
    return constrained_count(total, 1)


# print(their_count_change(10))


def their_count_change_2(total):

    # in this version we use a different (recursive) function to find power of two
    # and we use exactly THE SAME count_part function

    def highest_two(i, total):
        """A recursive variant of the highest of two function.
        We pass in i = 1 to start counting from bottom up
        And n is maximum amount we can't exceed
        """
        if i > total:
            return i // 2
        return highest_two(i*2, total)

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
            return count_part(n-m, m) + count_part(n, m//2)

    return count_part(total, highest_two(1, total))


# print(their_count_change_2(10))


print("-------------------- Q4 - MISSING DIGITS --------------------")


def missing_digits(n):
    """Takes in a sorted number and counts number of missing digts from 1 to n"""

    if n < 10:
        return 0

    last = n % 10
    penult = n // 10 % 10

    print(f'number is {n}, last is {last}, penult is {penult}')

    if last - penult <= 1:
        return 0 + missing_digits(n//10)
    else:
        return 1 + missing_digits(n//10*10 + last-1)


# print(missing_digits(3558))


def their_missing_digits(n):
    # what did they do differently?
    # instad of decremeing number by 1 on each recursive iteration, like I did, they just flat out calculated the difference between that num and the previous
    if n < 10:
        return 0
    last, rest = n % 10, n // 10
    print(f'number is {n}, last is {last}, rest is {rest}')
    return max(last - rest % 10 - 1, 0) + their_missing_digits(rest)


# print(their_missing_digits(3558))
print("-------------------- Q5 - HANOI --------------------")


def print_move(origin, destination):
    print(f'Move the top disk from rod {origin} to rod {destination}')


def move_stack(n, start, end):
    """Plays the game of Hanoi.
    n = number of disks
    start = pole where you start
    end = pole where you end
    """

    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "bad start/end"

    if n == 1:
        print_move(start, end)

    else:
        # move everything but the bottom-most disk out of the way
        other = 6 - start - end
        move_stack(n-1, start, other)
        # move the bottom most-disk
        print_move(start, end)
        # move the rest
        move_stack(n-1, other, end)


move_stack(3, 1, 3)
