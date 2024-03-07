package com.leetcode;

import com.common.ListNode;

/**
 * 19. Remove Nth Node From End of List
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 */
public class Problem19 {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode res = new ListNode(0, head);
        ListNode node1 = res, node2 = res;
        for (int i = 0; i < n; i++) node1 = node1.next;
        while (node1.next != null) {
            node1 = node1.next;
            node2 = node2.next;
        }
        node2.next = node2.next.next;
        return res.next;
    }
}
