# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
"""
엣지케이스
1.원소가 1개일때
2.지워야하는 원소가 마지막 원소일떄

1번일때는 None으로 return
2번일때는 prev_head를 구해서, prev_head.next=None으로.

여기서 눈여겨볼거는, 클래스 메서드 안에 내부메서드를 재정의하는거보다
클래스 멤버,메서드로 self.호출해서 하는게 더 낫다.(레퍼런스 참조때문에 원본값이 변하지않음. 배열이 아니라서.)
"""
class Solution:
    num = 0
    def dfs2(self,prev_head,head,cnt):
        if cnt == self.num:
            if head.next is None:
                prev_head.next = None
            head.val = head.next.val
            head.next = head.next.next
        try:
            self.dfs2(head,head.next,cnt+1)
        except:
            return
    
    def dfs(self,head,cnt):
        if head is None:
            self.num = cnt
            return
        self.dfs(head.next,cnt+1)
        
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head
        
        self.dfs(head,0)
        self.num = self.num // 2
        self.dfs2(head,head,0)


        return head
