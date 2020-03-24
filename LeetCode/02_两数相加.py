# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b, p, carry = l1, l2, None, 0
        while a or b:
            val = (a.val if a else 0) + (b.val if b else 0) + carry
            carry, val = int(val / 10) if val >= 10 else 0, val % 10
            p, p.val = a if a else b, val
            a, b = a.next if a else None, b.next if b else None
            p.next = a if a else b
        if carry:
            p.next = ListNode(carry)
        return l1
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode):
        def add(a, b, carry):
            if not (a or b):
                return ListNode(1) if carry else None
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            val = a.val + b.val + carry
            carry = 1 if val >= 10 else 0
            a.val = val % 10
            a.next = add(a.next, b.next, carry)
            return a
        return add(l1, l2, 0)
        
list1 = ListNode(7)
list1.next = None
list2 = ListNode(6)
list2.next = list1
list3 = ListNode(5)
list3.next = list2
print('{}'.format(list3))

list4 = ListNode(3)
list4.next = None
list5 = ListNode(9)
list5.next = list4
list6 = ListNode(8)
list6.next = list5
print('{}'.format(list6))

# solution = Solution()
# x = solution.addTwoNumbers(list3, list6)
# print('{}=={}=={}=={}'.format(x.val, x.next.val, x.next.next.val, x.next.next.next.val))

solution2 = Solution()
x2 = solution2.addTwoNumbers2(list3, list6)
print('{}=={}=={}=={}'.format(x2.val, x2.next.val, x2.next.next.val, x2.next.next.next.val))

#  输入：(5 -> 6 -> 7) + (8 -> 9 -> 3)
# 输出：3 -> 6 -> 1 -> 1
# 原因：765 + 398 = 1163