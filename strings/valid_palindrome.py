"""
Problem: Valid Palindrome
Platform: LeetCode (#125)
Difficulty: Easy

Summary:
Given a string, determine if it is a palindrome after:
- converting all uppercase letters to lowercase
- removing all non-alphanumeric characters

Approach:
- Traverse the string and build a new cleaned string:
    • keep only alphanumeric characters
    • convert each character to lowercase
- Compare the cleaned string with its reverse

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
- Used built-in string methods: isalnum() and lower()
- String slicing [::-1] is used for reversal
"""

def isPalindrome(self, s: str) -> bool:
    cleaned_string = self.clean_string(s)
    return cleaned_string[::-1] == cleaned_string

def clean_string(self, s: str) -> str:
    result = ""
    for i in s:
        if i.isalnum():
            result += i.lower()
    return result


#-----------------------
# Optimized Approach
#-----------------------
'''
Two-pointer technique:
'''