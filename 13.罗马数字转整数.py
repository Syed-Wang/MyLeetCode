#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rome = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        str_len = len(s)
        if str_len == 1:
            return rome[s]

        num = 0
        i = 0
        while i < str_len:
            if i == str_len - 1:
                num += rome[s[i]]
                return num
            elif rome[s[i]] >= rome[s[i + 1]]:
                num += rome[s[i]]
                i += 1
            else:
                num += rome[s[i + 1]] - rome[s[i]]
                if i + 2 < str_len:
                    i += 2
                else:
                    return num


# @lc code=end
