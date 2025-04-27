#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """解题思路：
        1. 双指针法，左右指针分别指向数组的两端，计算当前面积，并更新最大面积。
        2. 移动较小的指针，直到两个指针相遇为止。
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# @lc code=end
