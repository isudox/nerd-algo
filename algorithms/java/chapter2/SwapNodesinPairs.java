/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode res = new ListNode(0);
        ListNode curNode = res;
        res.next = head;
        while (curNode.next != null && curNode.next.next != null) {
            ListNode l = curNode.next, r = curNode.next.next;
            curNode.next = r;
            l.next = r.next;
            r.next = l;
            curNode = l;
        }
        return res.next;
    }
}