#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        """解题思路：
        1. 使用贪心算法，从大到小遍历罗马数字的值和对应的字符
        2. 如果当前数字大于等于罗马数字的值，就将对应的字符添加到结果中，并将数字减去对应的值
        3. 重复步骤2，直到数字减到0为止
        """
        roman_numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""
        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value
            if num == 0:
                break

        return result


# @lc code=end
