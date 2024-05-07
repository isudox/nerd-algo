package com.leetcode;

import com.common.ListNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 2487. Remove Nodes From Linked List
 * https://leetcode.com/problems/remove-nodes-from-linked-list
 */
public class Problem2487 {
    public ListNode removeNodes(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        List<ListNode> list = new ArrayList<>();
        ListNode p = head;
        while (p != null) {
            list.add(p);
            p = p.next;
        }
        boolean[] deleted = new boolean[list.size()];
        int max = list.get(list.size() - 1).val;
        for (int i = list.size() - 2; i >= 0; i--) {
            if (list.get(i).val < max) {
                deleted[i] = true;
            } else if (list.get(i).val > max) {
                max = list.get(i).val;
            }
        }
        ListNode dummy = new ListNode(0, head);
        p = dummy;
        for (int i = 0; i < list.size(); i++) {
            if (!deleted[i]) {
                p.next = list.get(i);
                p = p.next;
            }
        }
        return dummy.next;
    }
}
