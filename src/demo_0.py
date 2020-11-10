# Example of Recursion
    # and ways to do it with loops

def countdown(n):
    if n == 0:  # base case is n == 0
        return

    print(n)
    countdown(n-1)  # call itself and move towards the base case

countdown(5)

def countdown_for_loop(n):
    for i in range(n, 0, -1):
        print(i)

def countdown_while_loop(n):
    while n > 0:    # the base case is when n <= 0, we stop looping
        print(n)
        n = n - 1   # moving closer to the base case

# Example from Canvas
# Write a recursive search function that receives as input an array of integers and a target integer value.
# This function should return True if the target element exists in the array, and False otherwise.

# 1. What would be the base case(s) we'd have to consider for implementing this function?
# 2. How should our recursive solution converge on our base case(s)?

def search_iterative(nums, target):
    for num in nums:
        if num == target:
            return True

    return False

# we're calling search_recursion n times
def search_recursion(nums, target):
    # what are the base cases?
    if len(nums) == 0:
        return False

    num = nums[0]
    if num == target: # need to define num
        return True

    # slice off the first element that we just checked
    # slicing is O(n)
    search_recursion(nums[1:0], target) # move closer to base case by removing the first element that we just checked

    # we're running O(n) n times, so runtime is O(n^2)

# one way to reduce runtime is to pass in an index
def search_recursion_with_index(nums, target, start_index):
    # what are the base cases?
    if start_index == len(nums):
        return False

    num = nums[start_index]
    if num == target:
        return True

    search_recursion_with_index(nums, target, start_index + 1)

def binary_search(array, target):
    min = 0
    max = len(array) - 1
    while not max < min:
        guess = (max + min) // 2
        if array[guess] == target:
            return guess
        elif array[guess] < target:
            min = guess + 1
        else:
            max = guess - 1
    return -1

def binary_search_recursive(array, target, min, max):
    if max < min:
        return -1
    guess = (max + min) // 2
    if array[guess] == target:
        return guess
    elif array[guess] < target:
            min = guess + 1
    else:
        max = guess - 1
    return binary_search_recursive(array, target, min, max)

nums = [1, 4, 6, 14, 19, 22, 35, 39, 40]
target = 4
print(binary_search_recursive(nums, target, 0, len(nums) - 1))
print(binary_search(nums, target))