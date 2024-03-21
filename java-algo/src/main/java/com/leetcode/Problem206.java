package com.leetcode;

import com.common.ListNode;

/**
 * 206. Reverse Linked List
 * https://leetcode.com/problems/reverse-linked-list/
 */
public class Problem206 {
    public ListNode reverseList(ListNode head) {
        if (null == head || null == head.next) {
            return head;
        }
        ListNode rev = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return rev;
    }
}
