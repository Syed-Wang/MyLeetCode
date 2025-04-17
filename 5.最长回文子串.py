#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        char_to_index = {}
        left = 0
        max_left, max_right = 0, 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_to_index:
                left = max(left, char_to_index[s[right]])
            char_to_index[s[right]] = right
            len = right - left + 1
            if max_len < len:
                max_len = len
                max_left, max_right = left, right

        return s[max_left : max_right + 1]


# @lc code=end
