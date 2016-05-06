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
        ListNode result = new ListNode(0);
        int count = 0;
        while (l1.next != null && l2.next != null) {
            int sum = l1.val + l2.val;
            int carry = 0;
            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            } else {
                result.val = sum;
            }
        }
        return result;
    }
}

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int num1 = listNode2Num(l1);
        int num2 = listNode2Num(l2);
        int sum = num1 + num2;
        
        return num2ListNode(sum);
    }
    
    public int listNode2Num(ListNode listNode) {
        if (listNode == null) {
            return 0;
        }
        int num = 0;
        int digit = 0;
        do {
            num = 10 * num + listNode.val;
            digit++;
            listNode = listNode.next;
        } while (listNode.next != null)
        
        return num;
    }
    
    public ListNode num2ListNode(int num) {
        ListNode listNode = new ListNode(0);
        ListNode temp = new ListNode(0);
        while (num / 10 > 0) {
            int x = num % 10;
            num = num / 10;
            temp.val = x;
            temp.next = 
        }
    }
}