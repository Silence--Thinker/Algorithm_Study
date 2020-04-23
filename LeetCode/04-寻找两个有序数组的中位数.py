# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。 
# 
#  请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法

# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/di-gui-pai-chu-fa-jian-dan-yi-dong-de-ologminmnjie/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            temp = nums1
            nums1 = nums2
            nums2 = temp
            m = nums1
            n = nums2
        mid_m = (m - 1) // 2
        mid_n = (n - 1) // 2
        if m == 0:
            return nums2[mid_n] if (n % 2) == 1 else (nums2[mid_n] + nums2[mid_n + 1]) / 2
        if m == 1 or m == 2:
            if n < 3:
                nums1.extend(nums2)
            elif n % 2 == 1:
                nums1.extend(nums2[mid_n - 1:mid_n + 2])
            else:
                nums1.extend(nums2[mid_n - 1: mid_n + 3])
            nums1.sort()
            m = len(nums1)
            mid_m = (m - 1) // 2
            return nums1[mid_m] if m % 2 == 1 else (nums1[mid_m] + nums1[mid_m + 1]) / 2
        mid_np = mid_n if (n % 2) == 1 else mid_n + 1
        if nums1[mid_m] == nums2[mid_np]:
            return nums1[mid_m]
        if nums1[mid_m] < nums2[mid_np]:
            return self.findMedianSortedArrays(nums1[mid_m:], nums2[:n - mid_m])
        return self.findMedianSortedArrays(nums1[:m - mid_m], nums2[mid_m:])

solution = Solution()
nums1 = [10]
nums2 = [2, 5, 7, 8, 9, 10, 20, 30, 36]
x = solution.findMedianSortedArrays(nums1, nums2)
print('数组1: {} \n数组2: {}\n中位数是: {}'.format(nums1, nums2, x))


