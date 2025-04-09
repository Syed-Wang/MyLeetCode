#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """解题思路：
        1. 使用左右指针 left 和 right 表示当前窗口
        2. 用哈希表记录每个字符最后出现的位置
        3. 右指针不断向右移动扩大窗口
        4. 当遇到重复字符时，将左指针移动到重复字符上次出现位置的下一位
        5. 过程中更新最大窗口长度
        """
        char_to_index = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in char_to_index:
                left = max(left, char_to_index[s[right]] + 1)
            char_to_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length


# @lc code=end
