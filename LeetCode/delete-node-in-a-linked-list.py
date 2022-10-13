# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        현재 값을 다음노드의 값으로
        다음 노드를 다음다음 노드로.
        """
        node.val = node.next.val
        node.next = node.next.next
