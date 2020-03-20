package com.leetcode;

/**
 * 24. Swap Nodes in Pairs
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 * <p>
 * Given a linked list, swap every two adjacent nodes and return its head.
 * <p>
 * Example:
 * <p>
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 * Note:
 * <p>
 * Your algorithm should use only constant extra space.
 * You may not modify the values in the list's nodes, only nodes itself may be changed.
 */
public class SwapNodesinPairs {

    public ListNode swapPairs(ListNode head) {
        ListNode res = new ListNode(0);
        ListNode cur = res;
        res.next = head;
        while (cur.next != null && cur.next.next != null) {
            ListNode l = cur.next, r = cur.next.next;
            cur.next = r;
            l.next = r.next;
            r.next = l;
            cur = l;
        }
        return res.next;
    }
}
