/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode res = new ListNode(0);
        res.next = head;
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