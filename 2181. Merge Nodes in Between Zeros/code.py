# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
            flag = ListNode(0)
            current = flag
            sum_val = 0
            head = head.next  
            
            while head:
                if head.val == 0:
                    if sum_val > 0:
                        current.next = ListNode(sum_val)
                        current = current.next
                        sum_val = 0
                else:
                    sum_val += head.val
                head = head.next
            
            return flag.next
