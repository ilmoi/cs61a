basket = ['bread', 'potato', 'shovel', 'banana', 'yoghurt', 'meat', 'fish']

# add
basket.append('apple')

# remove
del basket[0]
basket.remove('apple')

print(basket)

# slicing
# start:stop:step

# select first 2
print(basket[:2])

# select the last 2
print(basket[-2:])

# select all but last 2
print(basket[:-2])

# select every nth elem
print(basket[::2])

# go in reverse
print(basket[::-1])
print(list(reversed(basket)))

# go in reverse to a point
# NOTE: start and stop need to be provided in reverse too (they are still in the same places though, so start is the first argument : stop : step)
print(basket[-2::-1])
print(basket[-2:-5:-1])

# shallow copy a list
# NOTE creates a separate object
basket2 = basket[:]
basket2.pop()
print(basket)
print(basket2)

print("-------------------- SLICE OBJ --------------------")

# create a slice object, if we wanted to re-use it on multiple lists
item_after_second = slice(2, 2+1)
print(basket[item_after_second])


print("-------------------- SLICE ASSIGNMENT --------------------")
# can be used to update a list with new values
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
nums[:4] = [1, 2, 3, 4]
print(nums)

# we can replace with a bigger chunk
nums[:4] = [1, 2, 3, 4, 5, 6, 7]
print(nums)

# or a smaller chunk
nums[:5] = [1]
print(nums)

print("-------------------- SLICE DELETION --------------------")
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
del nums[3:7]
print(nums)
del nums[::2]
print(nums)
