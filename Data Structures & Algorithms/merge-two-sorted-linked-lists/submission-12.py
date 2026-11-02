# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        # Prechádzame oba zoznamy, kým ani jeden nie je na konci
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        # Ak v jednom zo zoznamov zostali prvky, pripojíme ich na koniec
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next
                

        