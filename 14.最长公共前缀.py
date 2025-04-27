#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """解题思路：
        1. 如果字符串列表为空，返回空字符串
        2. 将第一个字符串作为前缀，遍历其他字符串
        3. 对于每个字符串，检查它是否以当前前缀开头，如果不是，则将前缀缩短到当前前缀的长度
        4. 如果前缀变为空，则返回空字符串
        5. 返回最终的前缀
        """
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# @lc code=end
