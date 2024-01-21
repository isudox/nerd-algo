package com.leetcode;

import com.common.ListNode;

/**
 * 82. Remove Duplicates from Sorted List II
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
 */
public class Problem82 {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode dummy = new ListNode(9999, head);
        ListNode a = dummy, b = head, c = head.next;
        while (c != null) {
            if (b.val != c.val) {
                a = b;
                b = c;
                c = c.next;
            } else {
                while (c != null && c.val == b.val) {
                    c = c.next;
                }
                b = c;
                a.next = b;
                if (c != null) c = c.next;
            }
        }
        return dummy.next;
    }
}
