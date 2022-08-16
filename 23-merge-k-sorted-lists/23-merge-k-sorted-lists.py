# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)              
        heap = []

        for n in lists:                      
            while n:                         
                heapq.heappush(heap, n.val)  
                n = n.next

        cur = dummy                         
        while heap:
            temp = ListNode(heapq.heappop(heap))  
            cur.next = temp                       
            cur = cur.next                        
        cur.next = None                          
        return dummy.next