class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.l1 = list1.sort()
        self.l2 = list2.sort()
        self.l3 = self.l1+self.l2
        return self.l3.sort()
    
    
