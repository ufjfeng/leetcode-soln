"""
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end
should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example, Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 2:
            return head
        h = ListNode(None)
        h.next = head
        p = h
        while p:
            p = self.reverseNextK(p, k)
        return h.next

    def reverseNextK(self, p, k):
        groupHead = p
        for i in range(k):
            if p.next:
                p = p.next
            else:
                return None
        firstNode = groupHead.next
        prev = groupHead
        curr = groupHead.next
        for i in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        firstNode.next = curr
        groupHead.next = prev
        return firstNode

