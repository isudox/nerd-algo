package com.leetcode;

import com.common.ListNode;

/**
 * 328. Odd Even Linked List
 * https://leetcode.com/problems/odd-even-linked-list/
 */
public class Problem328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return head;
        }
        ListNode p1 = head, p2 = head.next, p3 = p2;
        while (p2 != null && p2.next != null) {
            p1.next = p2.next;
            p2.next = p1.next.next;
            p1 = p1.next;
            p2 = p2.next;
        }
        p1.next = p3;
        return head;
    }
}
