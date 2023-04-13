package com.leetcode;

import com.common.ListNode;

/**
 * 160. Intersection of Two Linked Lists
 * https://leetcode.com/problems/intersection-of-two-linked-lists/
 */
public class Problem160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1 = headA, p2 = headB;
        int switched = 0;
        while (switched < 3) {
            if (p1 == p2) {
                return p1;
            }
            if (p1.next != null) {
                p1 = p1.next;
            } else {
                p1 = headB;
                switched++;
            }
            if (p2.next != null) {
                p2 = p2.next;
            } else {
                p2 = headA;
                switched++;
            }
        }
        return null;
    }
}
