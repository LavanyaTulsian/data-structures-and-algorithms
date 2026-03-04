"""
Problem: Palindrome Number
Platform: LeetCode
Difficulty: Easy

Problem Summary
---------------
Given an integer x, return True if x is a palindrome, and False otherwise.

A palindrome number reads the same forward and backward.

Examples
--------
Input: 121
Output: True
Explanation: 121 reversed is 121.

Input: -121
Output: False
Explanation: When reversed it becomes 121-, which is not a valid number format.

Input: 10
Output: False
Explanation: Reversed value becomes 01 which is not equal to 10.


Current Approach (String Conversion)
------------------------------------
1. Negative numbers cannot be palindromes, so return False immediately.
2. Convert the integer to a string.
3. Reverse the string using Python slicing.
4. Compare the reversed string with the original string.

If both are equal, the number is a palindrome.


Time Complexity -- O(n)
---------------
Where n is the number of digits in the integer.

Space Complexity -- O(n)
----------------
Because the integer is converted to a string and a reversed copy is created.
"""

# ----------------------
# Current Approach (String Conversion)
# ----------------------
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        a = str(x)
        reversed_string = a[::-1]

        if a == reversed_string:
            return True

        return False



# ----------------------
# Better Approach (Digit Manipulation)
# ----------------------
"""
Time Complexity (Better Approach): O(n)
Space Complexity (Better Approach): O(1)
"""
# We do this without converting the integer to a strng, which saves space.
