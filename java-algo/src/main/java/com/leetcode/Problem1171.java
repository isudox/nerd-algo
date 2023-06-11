package com.leetcode;

import com.common.ListNode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1171. Remove Zero Sum Consecutive Nodes from Linked List
 * https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
 */
public class Problem1171 {
    public ListNode removeZeroSumSublists(ListNode head) {
        if (head == null) {
            return null;
        }
        Map<Integer, ListNode> seen = new HashMap<>();
        ListNode cur = head;
        int sum = 0;
        while (cur != null) {
            sum += cur.val;
            if (sum == 0) {
                return removeZeroSumSublists(cur.next);
            }
            if (seen.containsKey(sum)) {
                ListNode last = seen.get(sum);
                last.next = cur.next;
                return removeZeroSumSublists(head);
            }
            seen.put(sum, cur);
            cur = cur.next;
        }
        return head;
    }
}
