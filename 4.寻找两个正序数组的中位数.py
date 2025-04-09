#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """解题思路：
        1. 确保第一个数组的长度小于或等于第二个数组
        2. 在较短的数组上进行二分查找，找到一个适当的分割点
        3. 根据分割点计算第二个数组的相应分割点
        4. 验证分割是否满足条件，调整分割点
        5. 根据总长度的奇偶性返回中位数
        """
# @lc code=end

