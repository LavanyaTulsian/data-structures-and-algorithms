"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy

Summary:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


# ----------------------
# Brute Force Approach
# ----------------------
"""
Time Complexity (Brute Force): O(n^2)
Space Complexity (Brute Force): O(1)
"""

def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]



# ----------------------
# Optimized Approach
# ----------------------
"""
Time Complexity (Optimized): O(n)
Space Complexity (Optimized): O(n)
"""

