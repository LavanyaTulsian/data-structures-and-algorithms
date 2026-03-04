"""
Problem: Longest Substring Without Repeating Characters
Platform: LeetCode
Difficulty: Medium

Problem Summary
---------------
Given a string `s`, find the length of the longest substring
that contains no repeating characters.

A substring must be contiguous (characters must appear next to each other).

Example:
Input:  s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3.


Brute Force Approach
--------------------
Idea:
- Start a substring at each index of the string.
- Expand the substring character by character until a duplicate appears.
- Use a list (or set) to track characters seen in the current substring.
- If a duplicate is encountered, stop expanding and move the starting index forward.
- Track the maximum length found.

Time Complexity: O(n^3)
Reason:
- For every starting index we potentially scan the rest of the string and then also check in the seen list again

Space Complexity: O(n)
Reason:
- We store characters seen in the current substring.

"""
# ----------------------
# Brute Force Approach
# ----------------------
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        marker = 0
        seen = []
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[j] not in seen:
                    marker = marker + 1
                    seen.append(s[j])
                    if marker > count:
                        count = marker
                else:
                    marker = 0
                    del seen[:]
                    break
        return count


# ----------------------
# Optimized Approach using Sliding window technique
# ----------------------
"""
Time Complexity (Brute Force): O(n)
Space Complexity (Brute Force): O(1)
"""
