#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """解题思路：
        1. 先判断符号，负数就取反，正数就不变
        2. 使用数学方法，取余数和整除来反转数字
        3. 判断反转后的数字是否在32位整数范围内，如果不在范围内就返回0
        """
        INT_MAX = 2**31 - 1
        MAX_DIV_10 = INT_MAX // 10
        sign = 1 if x >= 0 else -1
        abs_x = abs(x)
        reversed_x = 0

        while abs_x != 0:
            digit = abs_x % 10
            abs_x //= 10

            if reversed_x > MAX_DIV_10 or (
                reversed_x == MAX_DIV_10 and digit > INT_MAX % 10
            ):
                return 0

            reversed_x = reversed_x * 10 + digit

        return sign * reversed_x


# @lc code=end
