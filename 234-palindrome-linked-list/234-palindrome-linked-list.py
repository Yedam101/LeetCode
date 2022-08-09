# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        q = collections.deque()
        
        if not head:
            return True
        
        ListNode = head
        while ListNode:
            q.append(ListNode.val)
            ListNode = ListNode.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True
            
        