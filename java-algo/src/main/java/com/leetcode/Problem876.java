package com.leetcode;

import com.common.ListNode;

/**
 * 876. Middle of the Linked List
 * https://leetcode.com/problems/middle-of-the-linked-list/
 */
public class Problem876 {
    public ListNode middleNode(ListNode head) {
        int n = 0;
        ListNode p = head;
        while (p != null) {
            n++;
            p = p.next;
        }
        p = head;
        for (int i = 0; i < n / 2; i++) {
            p = p.next;
        }
        return p;
    }
}
