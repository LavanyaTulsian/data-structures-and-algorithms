"""
Problem: Add Two Numbers
Platform: LeetCode
Difficulty: Medium

Approach:
- Traverse both linked lists simultaneously.
- Add corresponding digits along with a carry.
- Create a new node for each computed digit.
- Use a dummy head node to simplify linked list construction.
- Continue until both lists are empty and carry is 0.

Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for singly-linked list. 
class ListNode(object): 
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # when we add two digits like 8 and 9 then we get 17, so we need to carry 1 to the next addition
        # we initialize carry to 0 at the beginning
        carry = 0
        #we make a new node with 0 as placeholder
        dummy = ListNode(0)
        # we use current to traverse dummy and keep track of the last node in the result list
        current = dummy

        while l1 or l2 or carry:

            if l1:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0

            if l2:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0

            total = value1 + value2 + carry

            carry = total // 10
            
            # since we are dealing with single digits, the modulo with 10 will always give us the last digit
            # which will be the number itself
            digit = total % 10

            new_node = ListNode(digit)
            current.next = new_node
            current = current.next

        # the first node is the placeholder we created at beginning before the loop
        # so we return dummy.next to get the actual head of the resulting linked list
        return dummy.next