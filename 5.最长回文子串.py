#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """解题思路：
        1. 回文串都是关于其中心对称的。
           中心可能是一个字符，也可能是两个字符之间的空隙。
        2. 字符串 s 中，总共有 2n - 1 个可能的中心点
          （n 个单字符中心和 n - 1 个双字符之间的中心）。
        3. 遍历这 2n - 1 个中心点，并以每个中心点为基准，
           向两边扩展，直到不再是回文串为止。
        4. 在扩展过程中，记录下找到的最长回文子串的起始和结束索引。
        """

        def expand_center(left, right):
            """从中心向两边扩展，返回回文串的长度"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        max_len = 1
        for i in range(len(s)):
            odd_len = expand_center(i, i)
            even_len = expand_center(i, i + 1)
            cur_max_len = max(odd_len, even_len)
            if cur_max_len > max_len:
                max_len = cur_max_len
                start = i - (max_len - 1) // 2

        return s[start : start + max_len]


# @lc code=end
