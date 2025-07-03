from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class LL:
    def mergeLinkedList(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        outputList = ListNode()
        cur = outputList
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if not list1:
            cur.next = list2
        if not list2:
            cur.next = list1

        return outputList.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
ll = LL()
print(ll.mergeLinkedList(l1, l2))