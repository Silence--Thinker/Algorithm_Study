#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pre = ListNode(0)
        newl = pre
        p = {}
        for i in range(len(lists)):
            node = lists[i]
            if not node is None:
                p[i] = node
        while p:
            min_index = min(p.keys())
            min_number = p[min_index].val
            for index in p.keys():
                node = p[index]
                if min_number > node.val:
                    min_number = node.val
                    min_index = index
            find_node = p[min_index]
            newl.next = find_node
            newl = find_node
            find_node = find_node.next
            p[min_index] = find_node
            if find_node is None:
                p.pop(min_index)
        return pre.next

    def mergeKLists_02(self, lists):
        # 使用堆队列的形式去解题
        import heapq
        pre = ListNode(0)
        newl = pre
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        # print (head)  # 堆队列，返回的是一个有序的数组
        while head:
            val, idx = heapq.heappop(head)
            newl.next = ListNode(val)
            newl = newl.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return pre.next
    



s = Solution()
s.mergeKLists_02([])                

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


