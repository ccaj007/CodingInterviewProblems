######################################
# DOESN'T WORK LOCALLY , ListNode
#
####################################

'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #dummy = ListNode
        cur = head

        cur = cur.next
        print(cur)        


head = [1,2,3,4,5]
n = 2
a = Solution()
a.removeNthFromEnd([1,2,3,4,5],n)

