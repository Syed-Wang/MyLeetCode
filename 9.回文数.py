#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """方法一：转为字符串
        str_x = str(x)
        re_str = str_x[::-1]
        return str_x == re_str
        """

        """方法二：数学方法
        1. 负数不是回文数
        2. 如果一个数字的最后一位是0，那么它的第一位只能是0
        3. 反转一半数字，比较反转后的数字和剩下的数字是否相等
        4. 反转数字的方式：取余和除法
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        # 当数字长度为奇数时，可以通过 reversed_num // 10 去除中间的数字
        return x == reversed_num or x == reversed_num // 10


# @lc code=end
