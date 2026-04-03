"""
Problem: Median of Two Sorted Arrays
Platform: LeetCode
Difficulty: Hard

Question:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Approach (Merge - O(m + n)):
- Use two pointers to merge both sorted arrays into a single sorted array.
- After merging, compute the median based on total length:
    • If even → average of two middle elements
    • If odd → middle element

Time Complexity: O(m + n)
Space Complexity: O(m + n)

Note:
This does not meet the optimal O(log(m+n)) requirement.
This is a foundational approach before optimizing further.
"""

from ast import List #required to use List type hinting in the function signature. Not in the Leetcode environment, but necessary for standalone code.

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    merge_nums = []
    i,j = 0,0

    # 2 way merge of the 2 sorted arrays
    while(i< m and j<n):
        if nums1[i] < nums2[j]:
            merge_nums.append(nums1[i])
            i+=1
        else:
            merge_nums.append(nums2[j])
            j+=1
    
    # If there are remaining elements in nums1 or nums2, we add them to merge_nums
    for k in range(i,m):
        merge_nums.append(nums1[k])
    for k in range(j,n):
        merge_nums.append(nums2[k])

    l = len(merge_nums)
    
    # Median calculation based on the length of the merged array
    if l % 2 == 0:
        return (merge_nums[l//2] + merge_nums[(l//2)-1])/2
    else:
        return merge_nums[l//2]
    

# ----------------------
# Optimized Approach
# ----------------------
'''
Below we will add the optimized approach
'''

