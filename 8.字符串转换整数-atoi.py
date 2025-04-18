#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        """解题思路：
        1. 去除前导空格
        2. 判断符号，正数和负数
        3. 遍历字符串，判断是否是数字
        4. 如果是数字，计算结果，判断是否越界
        5. 如果越界，返回最大值或最小值
        6. 返回结果
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        n: int = len(s)
        index = 0
        sign = 1
        result = 0

        while index < n and s[index] == " ":
            index += 1

        if index < n and (s[index] == "+" or s[index] == "-"):
            if s[index] == "-":
                sign = -1
            index += 1

        while index < n and s[index].isdigit():
            digit = int(s[index])

            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        return sign * result


# @lc code=end
