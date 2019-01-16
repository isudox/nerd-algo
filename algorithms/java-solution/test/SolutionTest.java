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
import org.junit.Test;
import utils.Converter;

import static org.junit.Assert.assertArrayEquals;

/**
 * Test algorithms with incomplete cases.
 */
public class SolutionTest {

    /**
     * 1. TwoSum
     */
    @Test
    public void testTwoSum() {
        TwoSum solution = new TwoSum();
        int[] nums = new int[]{1, 5, 8, 10, 23, 99};
        int target = 31;
        int[] res1 = solution.twoSum1(nums, target);
        int[] res2 = solution.twoSum2(nums, target);
        assertArrayEquals(new int[]{2, 4}, res1);
        assertArrayEquals(new int[]{2, 4}, res2);
    }

    /**
     * 2. Add Two Numbers
     */
    @Test
    public void testAddTwoNumbers() {
        AddTwoNumbers solution = new AddTwoNumbers();
        int[] arr1 = new int[]{2, 4, 3};
        int[] arr2 = new int[]{5, 6, 4};
        ListNode l1 = Converter.convertListNode(arr1);
        ListNode l2 = Converter.convertListNode(arr2);
        ListNode res1 = solution.addTwoNumbers1(l1, l2);
        ListNode res2 = solution.addTwoNumbers2(l1, l2);
        ListNode res = Converter.convertListNode(new int[]{7, 0, 8});
        assertArrayEquals(Converter.convertArray(res), Converter.convertArray(res1));
        assertArrayEquals(Converter.convertArray(res), Converter.convertArray(res2));
    }

    /**
     * 23. Merge k Sorted Lists
     */
    @Test
    public void testMergeKSortedLists() {
        MergeKSortedLists solution = new MergeKSortedLists();
        int[] i1 = new int[]{1, 4, 5};
        int[] i2 = new int[]{1, 3, 4};
        int[] i3 = new int[]{2, 6};
        ListNode l1 = Converter.convertListNode(i1);
        ListNode l2 = Converter.convertListNode(i2);
        ListNode l3 = Converter.convertListNode(i3);

        ListNode res = solution.mergeKLists(new ListNode[]{l1, l2, l3});
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4, 5, 6}, Converter.convertArray(res));
    }

}
