#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    # 把每个字母当成回文串的中心
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        self.res = ''
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i - 1:
                self.res = s[i + 1: j]
        for i in range(n):
            helper(i, i)        # 回文是奇数 eg: usu, 最中心数是s
            helper(i, i + 1)    # 回文是偶数 eg: suus, 最中心数是uu
        return self.res
    
    # 把每个字母当成回文串的结束
    def longestPalindrome2(self, s):
        n = len(s)
        max_str = ''
        def helper(s, i, j):
            n = len(s)
            mid = (i + j) // 2
            if i == j:
                return True
            while j >= 0 and i < n and s[i] == s[j] and j > i:
                i += 1
                j -= 1
            if mid == i or mid == j:
                return True
            return False
        
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # print('i = {}, {}, j={}, {}'.format(i, s[i], j, s[j]))
                    # 判断是否存在回文 不存在就找下一个，存在更新最长子串
                    if helper(s, i, j):
                        temp = s[i:j+1]
                        # print('i = {}, {}, j={}, {}=={}'.format(i, s[i], j, s[j], temp))
                        max_str = temp if len(temp) > len(max_str) else max_str
        
        return max_str

solution = Solution()
string = 'TTYYEPOPERYPT'
x = solution.longestPalindrome(string)
print('字符串: {}中, 最长子串是: {}'.format(string, x))

string2 = 'TTYYEPOOOPERYPT'
x2 = solution.longestPalindrome2(string2)
print('字符串: {}中, 最长子串是: {}'.format(string2, x2))

s = [ 1, 2 ,3 ]
print('{}, {}'.format(s, s[::-1]))