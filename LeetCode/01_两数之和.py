# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            a = target - nums[x]
            if a in nums:
                y = nums.index(a)
                if x == y:
                    continue
                else:
                    return x, y
                    break
            else:
                continue
    def twoSumHeight(self, nums, target):
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target-nums[x]], x
            else:
                d[nums[x]] = x
        pass

solution = Solution()
array = [1, 2, 3, 4, 9]
sum = 7
x = solution.twoSum(array, sum)
y = solution.twoSumHeight(array, sum)
print('{}数组中，和为{}的两个数的下标为{}'.format(array, sum, x))
print('{}数组中，和为{}的两个数的下标为{}'.format(array, sum, y))
        




