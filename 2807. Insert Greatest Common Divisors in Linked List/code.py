# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        def compute_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        while current and current.next:
            gcd_value = compute_gcd(current.val, current.next.val)
            
            new_node = ListNode(gcd_value)

            new_node.next = current.next
            current.next = new_node
            
            current = current.next.next
        
        return head