# --------------------------------------------
# LeetCode 1 - Two Sum
# --------------------------------------------

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # if the target isn't found in there then it prints an empty list

# --------------------------------------------
# Examples
# --------------------------------------------  

print(two_sum([2, 7, 11, 15], 9))  # returns [0, 1]
print()
print(two_sum([3, 2, 4], 6))  # returns [1, 2]
print()
print(two_sum([3, 3], 6))  # returns [0, 1]
print()
print(two_sum([1, 2, 3, 4, 5], 10))  # returns []