package com.leetcode;

import com.common.ListNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 2816. Double a Number Represented as a Linked List
 * https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
 */
public class Problem2816 {
    public ListNode doubleIt(ListNode head) {
        Deque<ListNode> q = new ArrayDeque<>();
        ListNode cur = head;
        while (cur != null) {
            q.offerLast(cur);
            cur = cur.next;
        }
        int add = 0;
        while (!q.isEmpty()) {
            ListNode tail = q.pollLast();
            tail.val = tail.val * 2 + add;
            add = tail.val / 10;
            tail.val %= 10;
        }
        return add == 0 ? head : new ListNode(add, head);
    }
}
