package com.leetcode;

import com.common.ListNode;

import java.util.HashSet;
import java.util.Set;

public class Problem3217 {
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        ListNode dummy = new ListNode(-1, head);
        ListNode cur = dummy, next = head;
        while (next != null) {
            if (set.contains(next.val)) {
                cur.next = next.next;
            } else {
                cur = next;
            }
            next = cur.next;
        }
        return dummy.next;
    }
}
