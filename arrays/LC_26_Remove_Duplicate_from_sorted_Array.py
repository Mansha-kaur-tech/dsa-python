# ---------------------------------------------
# LeetCode 26 - Remove Duplicates from Sorted Array
# ---------------------------------------------

def removeDuplicates(nums):
    j = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[j]:
            pass
        else:
            j += 1
            nums[j] = nums[i]

    return j + 1


# ---------------------------------------------
# Example 1
# ---------------------------------------------

nums1 = [1, 1, 2]

k1 = removeDuplicates(nums1)

print("Unique Elements:", k1)
print("Updated Array:", nums1[:k1])


# ---------------------------------------------
# Example 2
# ---------------------------------------------

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k2 = removeDuplicates(nums2)

print("Unique Elements:", k2)
print("Updated Array:", nums2[:k2])