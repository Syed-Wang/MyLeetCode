#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

# from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 解题思路：
        1. 使用哈希表存储数组元素及其索引
        2. 遍历数组，计算当前元素的补数（target - nums[i]）
        3. 检查补数是否在哈希表中
        4. 如果找到，返回当前索引和补数的索引
        5. 如果没有找到，将当前元素及其索引存入哈希表
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [index, num_to_index[complement]]
            num_to_index[num] = index
        return []


# @lc code=end
