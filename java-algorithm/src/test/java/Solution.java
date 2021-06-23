import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
*/
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null || left == right)
            return head;
        int pos = 0;
        ListNode dummy = new ListNode(0, head);
        ListNode ptr = dummy;
        List<ListNode> queue = new ArrayList<>();
        ListNode start = null;
        while (ptr != null) {
            if (pos == left - 1) {
                start = ptr;
            }
            if (left <= pos && pos <= right) {
                queue.add(ptr);
            }
            if (pos > right) {
                for (int i = queue.size() - 1; i > 0; i--) {
                    queue.get(i).next = queue.get(i - 1);
                }
                queue.get(0).next = ptr;
                start.next = queue.get(queue.size() - 1);
            } else {
                ptr = ptr.next;
                pos++;
            }
        }
        return dummy.next;
    }

    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
}
