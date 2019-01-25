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

package com.leetcode.util;


import com.leetcode.common.ListNode;

import java.util.Arrays;

/**
 * Convenient converters for LeetCode data structure.
 */
public final class Converter {

    /**
     * Convert an array to {@link ListNode}.
     *
     * @param nums An array of int.
     * @return ListNode
     */
    public static ListNode convertListNode(int[] nums) {
        int len = nums.length;

        if (len == 0) {
            return null;
        }

        ListNode node = new ListNode(0);
        node.val = nums[0];
        node.next = convertListNode(Arrays.copyOfRange(nums, 1, len));

        return node;
    }

    public static int[] convertArray(ListNode listNode) {
        if (null == listNode) {
            return null;
        }

        int size = getSize(listNode);
        int[] nums = new int[size];
        for (int i = 0; i < size; i++) {
            nums[i] = listNode.val;
            listNode = listNode.next;
        }

        return nums;
    }

    public static int getSize(ListNode listNode) {
        if (null == listNode) {
            return 0;
        }

        int length = 0;
        while (null != listNode) {
            length++;
            listNode = listNode.next;
        }

        return length;
    }

    public static String printListNode(ListNode listNode) {
        StringBuilder out = new StringBuilder();
        while (listNode != null) {
            out.append(listNode.val).append(", ");
            listNode = listNode.next;
        }
        return out.toString();
    }

    public static void main(String[] args) {
        int[] array = new int[]{1, 2, 3, 4, 5, 6};
        ListNode listNode = convertListNode(array);
        System.out.println(Arrays.toString(array));
        System.out.println(printListNode(listNode));
        System.out.println(Arrays.toString(convertArray(listNode)));
        System.out.println(getSize(listNode));
    }
}
