# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        연결리스트 문제.
        제일 중요한건 -> 포인터를 참조하였기때문에 참조한 값을 바꾸면 원본값에 영향을 끼친다.
        그래서 temp.next = temp.next.next를 하면 head의 next값이 변화하게 된다.
        근데, head.next로 진행하면, 원래 head 연결리스트를 살릴 수 없으니
        임시변수에 head를 할당하고, 이걸 next넘기면서 원하는곳에서 next = next.next로 한다.
        
        예외처리는 총 2곳을 해줘야하는데
        1. 노드가 1개인 연결리스트
        2. 첫번째 노드를 지워야하는 연결리스트
        에 대해 예외처리를 해주면 된다.
        """
        if head.next == None:
            return head.next
        
        idx = 1
        temp = head
        while True:
            if temp.next is None:
                break
            temp=temp.next
            idx+=1
        
        i=1
        temp=head
        while temp.next:
            if idx-n == 0:
                head = head.next
                break
            if idx-i == n:
                temp.next = temp.next.next
                break
            temp = temp.next
            i+=1
                
                
                
        return head
