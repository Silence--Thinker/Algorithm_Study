#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
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
        p = head
        result = ListNode(0)
        result.val = p.val
        result.next = None
        while p.next:
            new_node = ListNode(0)
            new_node.val = p.next.val
            new_node.next = result
            result = new_node
            p = p.next
        return result
# @lc code=end

