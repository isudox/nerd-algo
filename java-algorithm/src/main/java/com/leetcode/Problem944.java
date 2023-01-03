package com.leetcode;

/**
 * 944. Delete Columns to Make Sorted
 * https://leetcode.com/problems/delete-columns-to-make-sorted/
 */
public class Problem944 {
    public int minDeletionSize(String[] strs) {
        int ans = 0;
        int m = strs.length, n = strs[0].length();
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m - 1; i++) {
                if (strs[i].charAt(j) > strs[i + 1].charAt(j)) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
}
