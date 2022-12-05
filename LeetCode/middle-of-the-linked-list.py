# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    cnt = 0
    middleList: Optional[ListNode] = None
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        self.getNum(head)
        self.getMiddle(head,0)
        return self.middleList

    def getMiddle(self,head,c):
        c = 0
        while head:
            if c == self.cnt//2:
                self.middleList = head
                break
            c+=1
            head = head.next


    def getNum(self,head):
        self.cnt+=1
        if head.next is None:
            return
        self.getNum(head.next)
