"""
Most interpreters inplemented as an infinite loop: read-eval-print

Guerrilla 05

>> people(name, age, state, hobby): a person on Fakebook

>> posts(post id, poster, text, time): a post with its creator and creation time (in
minutes, starting at 0)

>> likes(post id, name, time): a like – post id of the post that was liked, name of
person who liked the post, and time (in minutes) of like

>> requests(friend1, friend2): a friend request from friend1 to friend2



2.1
select * from people where age < 26;

2.2
select post_id, name, time from posts where time < 230;

2.3
t1
SELECT post_id, name
FROM people, posts
WHERE poster = name;

t2
SELECT post_id
FROM t1, likes
WHERE likes.post_id = t1.post_id AND likes.name = postst1.name;

2.4
friends
SELECT *
FROM requests as r1, requests as r2
WHERE r1.friend1 = r2.friend2 AND r1.friend2 = r2.friend1;

2.5
SELECT friend1, count(*) as cnt
FROM friends
GROUP BY friend1
HAVING cnt > 4;

2.6
wills_friends
select friend2 as name
from friends
WHERE friend1 = will

select state count(*) as cnt
from people, wills_friends
where people.name = wills_friends.name
group by state

2.7
SELECT DISTINCT text
FROM posts, likes
WHERE posts.post_id = likes.post_id AND likes.time <= posts.time +2

2.8
select p1.name, p2.name, p1.hobby
from people as p1, people as p2
where p1.name < p2.name and p1.hobby = p2.hobby;

2.9
select state, count(*)
from people
group by state
order by count(*) desc

2.10
insert into requests(friend1, friend2) VALUES ("Denero", "Hilfy");

2.11
insert into requests(friend1, friend2) SELECT ('Denero', name FROM likes WHERE post_id = 349);

2.12
UPDATE people
SET hobby = "CS"
WHERE name = "joe";

2.13
CREATE TABLE num_likes AS
SELECT
    posts.poster AS name,
    posts.post_id AS post_id,
    COUNT(likes.name) AS number
FROM posts, likes
WHERE posts.post_id = likes.post_id
GROUP BY posts.post_id --Funny I thought you couldn't do that with sql and you had to group by all non-aggregated columns, but maybe I'm wrong

2.14
DELETE
FROM num_likes
WHERE number <= 4 AND name = "Carolyn"

2.15
CREATE TABLE privacy(name, visibility DEFAULT "everyone");

2.16
INSERT INTO privacy (name) VALUES ('Hermish');

"""


def fib_memo(n):
    cache = {}
    cache[0], cache[1] = 0, 1

    def mem(n):
        if n not in cache:
            cache[n] = mem(n-2) + mem(n-1)
        # initially forgot to return cache - really important
        return cache[n]

    return mem(n)


# print(fib_memo(7))


def lcs(a, b):
    # LCS = longest common subsequence
    """Finds the longest common subsequence between two strings a and b."""
    # very painful implementation - exponential both time and space complexity (in fact even worse than exponential - we have 2**n frames +_we make copies of lists in each which is linear)

    if len(a) == 0 or len(b) == 0:
        return 0
    elif a[0] == b[0]:
        return 1 + lcs(a[1:], b[1:])
    else:
        return max(lcs(a, b[1:]), lcs(a[1:], b))


# print(lcs('gucci', 'louis'))


def faster_lcs(a, b):
    # based on indices - still 2**n calls (exponential), but we no longer copy the list so this is quicker
    def helper(i, j):
        if i == len(a) or j == len(b):
            return 0
        elif a[i] == b[j]:
            return 1 + helper(i+1, j+1)
        else:
            return max(helper(i, j+1), helper(i+1, j))
    return helper(0, 0)


# print(faster_lcs('gucci', 'louis'))


def memo_lcs(a, b):
    # in the above functions we perform a lot of repeated work, let's cache it
    cache = {}

    # my version
    # def helper(i, j):
    #     if i == len(a) or j == len(b):
    #         return 0
    #     elif a[i] == b[j]:
    #         return 1 + helper(i+1, j+1)
    #     else:
    #         r1 = cache.get((i, j+1), helper(i, j+1))
    #         r2 = cache.get((i+1, j), helper(i+1, j))
    #         return max(r1, r2)

    # their version
    def helper(i, j):
        # time/space complexity = total number of unqiue pairs of inputs, ie i*jxx or n**2

        # NOTE - this is key. if (i,j) is in the cash we don't need to redo all the work!
        if (i, j) in cache:
            return cache[(i, j)]

        if i == len(a) or j == len(b):
            cache[(i, j)] = 0  # makes sense, should have stored
        elif a[i] == b[j]:
            cache[(i, j)] = 1 + helper(i+1, j+1)  # makes sense, should have stored
        else:
            cache[(i, j)] = max(helper(i, j+1), helper(i+1, j))
        return cache[(i, j)]  # notice you only RETURN ONCE

    return helper(0, 0)


# print(memo_lcs('gucci', 'louis'))


def dyn_lcs(a, b):


print(memo_lcs('gucci', 'louis'))
