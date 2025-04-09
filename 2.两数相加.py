#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """解题思路：
        1. 初始化一个虚拟头节点和当前节点指针，用于构建结果链表
        2. 初始化进位变量 carry 为 0
        3. 遍历两个链表，直到两个链表都为空且进位为 0
        4. 在每次迭代中，计算当前位的和，并更新进位
        5. 将当前位的和添加到结果链表中
        6. 返回结果链表的头节点
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


# @lc code=end
