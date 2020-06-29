# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s): # 1、遍历解法
        """
        :type s: str
        :rtype: int
        """
        longStr = set([])
        curStr = set([])
        max = 0
        for i in range(len(s)):
            longStr = set(s[i])
            curStr = set(s[i])
            for j in range(i + 1, len(s)):
                longStr.add(s[j])
                if len(longStr) > len(curStr):
                    curStr.add(s[j])
                else:
                    break
            if len(longStr) > max:
                max = len(longStr)
        return max

    def lengthOfLongestSubstring2(self, s): # 2、滑块解法
        start = 0
        end = 0
        max_length = 0
        strSet = set()
        while start < len(s) and end < len(s):
            lenStr = len(strSet)
            strSet.add(s[end])
            if len(strSet) == lenStr: # 有重复
                strSet.remove(s[start])
                start += 1
            else: # 没有重复
                end += 1
                max_length = max(max_length, end - start)
        return max_length
    
    def lengthOfLongestSubstring3(self, s): # 3、进出栈解法
        s_to_list = list(s)
        stack = []
        max_length = 0
        for item in s_to_list:
            if item in stack:
                index = stack.index(item)
                stack = stack[index + 1:]
                stack.append(item)
            else:
                stack.append(item)
                max_length = max(max_length, len(stack))
        return max_length

solution = Solution()
string = 'abcabcbb'
x = solution.lengthOfLongestSubstring(string)
print('字符串{}中，无重复字符的最长子串长度为：{}'.format(string, x))

x2 = solution.lengthOfLongestSubstring2(string)
print('字符串{}中，无重复字符的最长子串长度为：{}'.format(string, x2))

x3 = solution.lengthOfLongestSubstring3(string)
print('字符串{}中，无重复字符的最长子串长度为：{}'.format(string, x3))
