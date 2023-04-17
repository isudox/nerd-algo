package com.leetcode;

/**
 * 1157. Online Majority Element In Subarray
 */
public class Problem1157 {
    static class MajorityChecker {
        int[] arr;

        public MajorityChecker(int[] arr) {
            this.arr = arr;
        }

        public int query(int left, int right, int threshold) {
            int[] counter = new int[20001];
            for (int i = left; i <= right; i++) {
                if (++counter[arr[i]] >= threshold) {
                    return arr[i];
                }
            }
            return -1;
        }
    }
}
