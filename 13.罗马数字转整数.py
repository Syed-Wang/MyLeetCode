#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """解题思路：
        1. 从右到左遍历字符串，记录当前字符的值和前一个字符的值
        2. 如果当前字符的值小于前一个字符的值，则减去当前字符的值，否则加上当前字符的值
        """
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_values[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total


# @lc code=end
