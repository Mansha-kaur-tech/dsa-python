"""
LeetCode 1929 - Concatenation of Array

Difficulty: Easy

Problem:
Given an integer array nums,
return the concatenation of the array with itself.

Example:
Input: [1,2,1]
Output: [1,2,1,1,2,1]

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def getConcatenation(self, nums):
        return nums * 2


# -------------------------
# Test Cases
# -------------------------

solution = Solution()

print(solution.getConcatenation([1,2,1]))
print(solution.getConcatenation([1,3,2,1]))
print(solution.getConcatenation([5,7]))