#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """解题思路：
        1. 如果 numRows 为 1 或者大于等于字符串长度，
           则直接返回原字符串。
        2. 创建一个长度为 numRows 的列表 rows，用于存储每一行的字符。
        3. 使用一个变量 cur_row 来表示当前行的索引，
           另一个变量 direction 来表示当前的方向（向下或向上）。
        4. 遍历字符串 s 中的每个字符，将其添加到对应的行中。
        5. 当到达第一行或最后一行时，改变方向。
        6. 最后，将所有行的字符连接起来，返回结果。
        """

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row = 0
        direction = 1

        for char in s:
            rows[cur_row] += char
            if cur_row == 0:
                direction = 1
            elif cur_row == numRows - 1:
                direction = -1
            cur_row += direction

        return "".join(rows)


# @lc code=end
