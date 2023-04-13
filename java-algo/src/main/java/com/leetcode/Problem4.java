package com.leetcode;

/**
 * 4. Median of Two Sorted Arrays
 * https://leetcode.com/problems/median-of-two-sorted-arrays/
 * <p>
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * <p>
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)).
 * <p>
 * You may assume nums1 and nums2 cannot be both empty.
 * <p>
 * Example 1:
 *
 * <pre>
 * nums1 = [1, 3]
 * nums2 = [2]
 *
 * The median is 2.0
 * </pre>
 * <p>
 * Example 2:
 *
 * <pre>
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 *
 * The median is (2 + 3)/2 = 2.5
 * </pre>
 */
public class Problem4 {
    
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m == 0 && n == 0) return 0;
        int len = m + n;
        int[] ints = new int[len];
        int i = 0, j = 0;
        for (int index = 0; index < len; index++) {
            if (i < m && j < n) {
                if (nums1[i] < nums2[j]) {
                    ints[index] = nums1[i++];
                } else {
                    ints[index] = nums2[j++];
                }
            } else {
                if (i < m) {
                    ints[index] = nums1[i++];
                }
                if (j < n) {
                    ints[index] = nums2[j++];
                }
            }
        }
        if (len % 2 == 0) {
            return (ints[len / 2 - 1] + ints[len / 2]) / 2.0;
        } else {
            return ints[len / 2];
        }
    }
}
