package com.leetcode;

import com.common.ListNode;

/**
 * 1669. Merge In Between Linked Lists
 * https://leetcode.com/problems/merge-in-between-linked-lists/
 */
public class Problem1669 {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode tail = list2;
        while (tail.next != null) {
            tail = tail.next;
        }
        ListNode dummy = new ListNode(-1, list1);
        ListNode cur = list1, pre = dummy;
        for (int i = 0; i <= b; i++) {
            if (i == a) {
                pre.next = list2;
            }
            if (i == b) {
                tail.next = cur.next;
                break;
            }
            pre = cur;
            cur = cur.next;
        }
        return dummy.next;
    }
}
