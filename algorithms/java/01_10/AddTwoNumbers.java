/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.math.BigInteger;
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        BigInteger sum = listNode2Num(l1).add(listNode2Num(l2));
        if (BigInteger.ZERO.compareTo(sum) == 0) {
            return new ListNode(0);
        }

        return num2ListNode(sum);
    }

    public BigInteger listNode2Num(ListNode listNode) {
        if (listNode == null) {
            return BigInteger.valueOf(0);
        }

        return BigInteger.valueOf(listNode.val).add(listNode2Num(listNode.next)
                                                    .multiply(BigInteger.valueOf(10)));
    }

    public ListNode num2ListNode(BigInteger num) {
        ListNode listNode = new ListNode(0);
        if (BigInteger.ZERO.compareTo(num) == 0) {
            return null;
        }

        listNode.val = num.mod(BigInteger.valueOf(10)).intValue();
        listNode.next = num2ListNode(num.divide(BigInteger.valueOf(10)));

        return listNode;
    }
}
