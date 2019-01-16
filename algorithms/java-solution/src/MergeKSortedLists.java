/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2017-2019 sudoz
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 */

import common.ListNode;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * <p>
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * <p>
 * Example:
 *
 * <pre>
 *     Input:
 *     [
 *       1->4->5,
 *       1->3->4,
 *       2->6
 *     ]
 *     Output: 1->1->2->3->4->4->5->6
 * </pre>
 */
public class MergeKSortedLists {

    /**
     * The nerd approach :(
     * Time complexity:
     */
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode res = new ListNode(0);
        ListNode cur = res;
        List<Integer> nums = new ArrayList<>();

        for (ListNode l : lists) {
            while (null != l) {
                nums.add(l.val);
                l = l.next;
            }
        }

        while (nums.size() > 0) {
            cur.next = new ListNode(min(nums));
            cur = cur.next;
        }

        return res.next;
    }

    private int min(List<Integer> nums) {
        int min = nums.get(0);

        for (Integer num : nums) {
            if (num < min) {
                min = num;
            }
        }

        nums.remove(nums.indexOf(min));

        return min;
    }
}
