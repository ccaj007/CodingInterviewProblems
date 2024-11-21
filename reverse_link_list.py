'''
https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 
solution: https://www.youtube.com/watch?v=G0_I-ZF0S38


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


head = [1,2,3,4,5]
a=Solution()
a.reverseList(head)
