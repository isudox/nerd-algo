package com.leetcode;

import com.common.ListNode;

/**
 * 21. Merge Two Sorted Lists
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */
public class Problem21 {

    public ListNode mergeTwoLists1(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode ptr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                ptr.next = l1;
                l1 = l1.next;
            } else {
                ptr.next = l2;
                l2 = l2.next;
            }
            ptr = ptr.next;
        }
        if (l1 == null)
            ptr.next = l2;
        else
            ptr.next = l1;
        return dummy.next;
    }
}
