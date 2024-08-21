/*
 * @lc app=leetcode.cn id=3 lang=c
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
int lengthOfLongestSubstring(char* s)
{
    int n = strlen(s);
    int map[128] = { 0 }; // 用于记录字符最后出现的位置，类似于哈希表
    int left = 0, right = 0;
    int maxLength = 0;

    while (right < n) {
        char currentChar = s[right]; // 当前字符
        if (map[currentChar] > 0) { // 如果当前字符已经出现过
            left = (map[currentChar] > left) ? map[currentChar] : left; // 如果当前字符上次出现的位置在left右边，则更新left
        }
        map[currentChar] = right + 1; // 更新字符最后出现的位置
        maxLength = (maxLength > (right - left + 1)) ? maxLength : (right - left + 1);
        right++;
    }

    return maxLength;
}
// @lc code=end
