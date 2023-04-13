package com.leetcode;

import com.common.ListNode;

/**
 * 61. Rotate List
 * https://leetcode.com/problems/rotate-list/
 */
public class Problem61 {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        int n = 0;
        ListNode p = new ListNode(0, head);
        while (p.next != null) {
            n++;
            p = p.next;
        }
        ListNode tail = p;
        k = k % n;
        if (k == 0) return head;
        p = new ListNode(0, head);
        for (int i = 0; i < n - k; i++) {
            p = p.next;
        }
        ListNode ans = p.next;
        p.next = null;
        tail.next = head;
        return ans;
    }
}
