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

def isPalindrome(self, x):
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
Time Complexity (Better Approach): O(n) - because we potentially reverse all digits of the number.
Space Complexity (Better Approach): O(1) - we only use a constant amount of space to store the reversed number and the original number.
"""
# We do this without converting the integer to a strng, which saves space.

def isPalindrome(self, x):
    if x < 0:
        return False
    a = x
    reverse_val = 0
    while x > 0:   
        last_digit = x % 10
        # We are basically shifting the digits of reverse_val to the left by multiplying by 10 and then
        # adding the last_digit to it. This way we are constructing the reversed number.
        # Suppose we have 123 and we want to reverse it. Initially reverse_val is 0.
        # In the first iteration, last_digit will be 3 and reverse_val will become 0*10 + 3 = 3.
        # In the second iteration, last_digit will be 2 and reverse_val will become 3*10 + 2 = 32.
        # In the third iteration, last_digit will be 1 and reverse_val will become 32*10 + 1 = 321.
        # This is how we get the reversed number without converting to string.
        reverse_val = reverse_val * 10 + last_digit
        x = x // 10
    if reverse_val == a:
        return True
    return False