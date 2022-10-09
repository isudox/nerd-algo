package com.leetcode;

import java.util.Arrays;

/**
 * 870. Advantage Shuffle
 * https://leetcode.com/problems/advantage-shuffle/
 */
public class Problem870 {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        Integer[] idx1 = new Integer[nums1.length];
        Integer[] idx2 = new Integer[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            idx1[i] = i;
            idx2[i] = i;
        }
        Arrays.sort(idx1, (i, j) -> nums1[i] - nums1[j]);
        Arrays.sort(idx2, (i, j) -> nums2[i] - nums2[j]);
        int lo = 0, hi = nums1.length - 1;
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            if (nums1[idx1[i]] > nums2[idx2[lo]]) {
                ans[idx2[lo++]] = nums1[idx1[i]];
            } else {
                ans[idx2[hi--]] = nums1[idx1[i]];
            }
        }
        return ans;
    }
}
