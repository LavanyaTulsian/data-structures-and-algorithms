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

class Solution(object):
    def twoSum(self, nums, target):
        # We use a dictionary to store previously seen numbers.
        # Key   → number
        # Value → its index in the array
        seen = {} 
        for i in range(len(nums)):
            #we see if the difference between the target and current value, which will give us the required number to reach the target
            diff = target - nums[i] 
            if diff in seen:
                # if the diff is in seen then we return the current index and the index of the diff which is stored in seen
                # Dictionary lookup runs in average O(1) time, so this check is efficient.
                return [seen[diff],i]
            # if diff is not in seen then we add the current number as key and its index as the value to the seen dictionary
            seen[nums[i]] = i

# We check for the complement before inserting the current number.
# This prevents using the same element twice.
# If the current number equals its complement (e.g., target = 6, num = 3),
# the first occurrence is already stored in `seen`, and we return its index.
# If duplicates appear later, the dictionary simply updates the stored index,
# which does not affect correctness because a valid pair would have already returned.