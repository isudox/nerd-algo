/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
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