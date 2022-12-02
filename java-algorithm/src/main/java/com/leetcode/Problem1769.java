package com.leetcode;

/**
 * 1769. Minimum Number of Operations to Move All Balls to Each Box
 * https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
 */
public class Problem1769 {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] ans = new int[n];
        int[] left = new int[n];  // left[i]: the count of `1` before boxes[i]
        int[] right = new int[n]; // right[i]: the count of `1` after boxes[i]
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1] + (boxes.charAt(i - 1) - '0');
            if (boxes.charAt(i) - '0' > 0) {
                ans[0] += i;
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            right[i] = right[i + 1] + (boxes.charAt(i + 1) - '0');
        }
        for (int i = 1; i < n; i++) {
            ans[i] = ans[i - 1] + left[i] - right[i - 1];
        }
        return ans;
    }
}
