package com.leetcode;

import com.common.ListNode;

/**
 * 143. Reorder List
 * https://leetcode.com/problems/reorder-list/
 */
public class Problem143 {
    public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }
        int n = 0;
        ListNode p = head;
        while (p != null) {
            n++;
            p = p.next;
        }
        p = head;
        for (int i = 0; i < (n - 1) / 2; i++) {
            p = p.next;
        }
        ListNode rev = reverse(p.next);
        p.next = null;
        while (rev != null) {
            ListNode next0 = head.next;
            ListNode next1 = rev.next;
            head.next = rev;
            rev.next = next0;
            head = next0;
            rev = next1;
        }
    }

    private ListNode reverse(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        ListNode rev = reverse(head.next);
        head.next.next = head;
        head.next = null;
        return rev;
    }
}
