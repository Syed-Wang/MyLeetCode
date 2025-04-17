#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """解题思路：
        1. 确保第一个数组的长度小于或等于第二个数组，在长度最小的数组上操作达到最优时间复杂度
        2. 在较短的数组上进行二分查找，找到一个适当的分割点，同时计算出第二个数组的相应分割点
           使得左半部分的最大值小于等于另一个数组右半部分的最小值
        3. 验证分割是否满足条件，调整分割点
        4. 根据总长度的奇偶性返回中位数
        """

        # 确保 nums1 的长度较短
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax = 0, m
        half_len = (m + n + 1) // 2  # +1是为奇数长度时，左半部分多一个元素，即中位数

        # 找分割点
        while imin <= imax:
            i = (imin + imax) // 2  # nums1分到左半部分的元素个数
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:  # 先检查i边界条件
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # 找到合适的分割点
                # 计算左半部分的最大值
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left

                # 计算右半部分的最小值
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0


# @lc code=end
