#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        newl = None
        p = {}
        for i in len(lists):
            node = lists[i]
            p[i] = node
        while p:
            min = 0
            min_index = 0
            for index in p.keys:
                node = p[index]
                if min > node.val:
                    min = node.val
                    min_index = i
            if newl is None:
                newl = p[min_index]
            else:
                newl.val = p[min_index].val
                newl.next = p[min_index].next
            p[min_index] = p[min_index].next
            if p[min_index] is None:
                p.pop(min_index)
        newl.next = None



                

# @lc code=end

elements = []
elements.append(1)
elements.append(2)
print(elements)
print(min(elements))

dict = { 'age': 20}
print (dict)
print (dict.pop('age'))
print (dict)


