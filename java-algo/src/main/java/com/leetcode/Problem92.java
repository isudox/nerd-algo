package com.leetcode;

import com.common.ListNode;

import java.util.ArrayList;
import java.util.List;

public class Problem92 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null || left == right)
            return head;
        int pos = 0;
        ListNode dummy = new ListNode(0, head), p = dummy, start = null, end = null;
        List<ListNode> queue = new ArrayList<>();
        while (p != null) {
            if (pos == left - 1) {
                start = p;
            } else if (left <= pos && pos <= right) {
                queue.add(p);
                if (pos == right)
                    end = p.next;
            }
            p = p.next;
            pos++;
        }
        for (int i = queue.size() - 1; i > 0; i--) {
            queue.get(i).next = queue.get(i - 1);
        }
        queue.get(0).next = end;
        start.next = queue.get(queue.size() - 1);
        return dummy.next;
    }

    public ListNode reverseBetween2(ListNode head, int left, int right) {
        if (head == null || head.next == null || left == right)
            return head;
        int pos = 0;
        ListNode dummy = new ListNode(0, head), p = dummy, start = null, end = null;
        while (p != null) {
            if (pos == left - 1)
                start = p;
            if (pos == right)
                end = p.next;
            p = p.next;
            pos++;
        }
        helper(start, end);
        return dummy.next;
    }

    private void helper(ListNode leftNode, ListNode rightNode) {
        ListNode p1 = null, p2 = leftNode.next;
        while (p2 != rightNode) {
            ListNode nextNode = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = nextNode;
        }
        leftNode.next.next = rightNode;
        leftNode.next = p1;
    }
}
