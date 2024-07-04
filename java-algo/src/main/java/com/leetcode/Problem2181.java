package com.leetcode;

import com.common.*;

/**
 * 2181. Merge Nodes in Between Zeros
 * https://leetcode.com/problems/merge-nodes-in-between-zeros/
 */
public class Problem2181 {
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy = new ListNode(0), p = dummy;
        head = head.next;
        int sum = 0;
        while (head != null) {
            if (head.val == 0) {
                p.next = new ListNode(sum);
                p = p.next;
                sum = 0;
            } else {
                sum += head.val;
            }
            head = head.next;
        }
        return dummy.next;
    }
}
