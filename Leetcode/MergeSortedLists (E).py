# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        else:
            return list1
        if list1.val > list2.val:
            mergedHead = list2
            list2 = list2.next
        else:
            mergedHead = list1
            list1 = list1.next
        curr = mergedHead
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next 
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 != None:
            curr.next = list1
        if list2 != None:
            curr.next = list2
        return mergedHead