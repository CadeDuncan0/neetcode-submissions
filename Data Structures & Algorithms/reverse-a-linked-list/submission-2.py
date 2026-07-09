# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        listValues = []

        curr = head
        while curr is not None:
            listValues.append(curr.val)
            curr = curr.next 

        reversedList = ListNode()
        currNode = reversedList
        for i in range(len(listValues) - 1, 0, -1):
            currNode.val = listValues[i]
            currNode.next = ListNode()

            currNode = currNode.next

        currNode.val = listValues[0]

            

        return reversedList