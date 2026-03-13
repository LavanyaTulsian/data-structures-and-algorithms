"""
Problem: Roman to Integer
Platform: LeetCode
Difficulty: Easy

Problem Summary:
Given a Roman numeral string, convert it to an integer.

Approach:
- Map each Roman symbol to its integer value.
- Traverse the string from right to left.
- Add the value if the current symbol is greater than or equal to the symbol on its right.
- Otherwise subtract it.

Key Rule:
Smaller value before a larger value means subtraction.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def romanToInt(self, s):
    total = 0
    symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in range(len(s)-1,-1,-1):
        if i==(len(s)-1):
            total = symbol[s[i]]
        elif symbol[s[i]] >= symbol[s[i+1]]:
            total = total + symbol[s[i]]
        else:
            total = total - symbol[s[i]]
    return total