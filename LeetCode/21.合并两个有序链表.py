#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        p = None
        while p1 or p2:
            temp = None
            if p1.val > p2.val:
                temp = p2
                p2 = p2.next
            else:
                temp = p1
                p1 = p1.next
            if p is None:
                p = temp
            else:
                p.val = temp
                p.next = temp
        p.next = None
        return p

# @lc code=end

