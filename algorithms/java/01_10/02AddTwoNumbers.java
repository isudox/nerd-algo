/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int num1 = listNode2Num(l1);
        int num2 = listNode2Num(l2);
        int sum = num1 + num2;

        if (sum == 0) {
            return new ListNode(0);
        }

        return num2ListNode(sum);
    }

    public int listNode2Num(ListNode listNode) {
        if (listNode == null) {
            return 0;
        }

        return listNode.val + listNode2Num(listNode.next) * 10;
    }

    public ListNode num2ListNode(int num) {
        ListNode listNode = new ListNode(0);
        if (num == 0) {
            return null;
        }

        listNode.val = num % 10;
        listNode.next = num2ListNode(num / 10);

        return listNode;
    }
}
