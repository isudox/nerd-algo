package com.leetcode.solution;

/**
 * 21. Merge Two Sorted Lists
 * https://leetcode.com/problems/merge-two-sorted-lists/
 *
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 *
 * Example:
 *
 * Input: 1->2->4, 1->3->4
 * Output: 1->1->2->3->4->4
 */
public class MergeTwoSortedLists {

    public ListNode mergeTwoLists1(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode temp = res;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                temp.next = l1;
                l1 = l1.next;
            } else {
                temp.next = l2;
                l2 = l2.next;
            }
            temp = temp.next;
        }
        if (l1 == null) temp.next = l2;
        else temp.next = l1;
        return res.next;
    }

    public ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        pickListNode(l1, l2, res);

        return res.next;
    }

    private void pickListNode(ListNode l1, ListNode l2, ListNode res) {
        if (l1 == null || l2 == null) {
            res.next = l1 == null ? l2 : l1;
        } else if (l1.val < l2.val) {
            res.next = l1;
            l1 = l1.next;
            pickListNode(l1, l2, res.next);
        } else {
            res.next = l2;
            l2 = l2.next;
            pickListNode(l1, l2, res.next);
        }
    }
}