package com.leetcode;

/**
 * 1640. Check Array Formation Through Concatenation
 * https://leetcode.com/problems/check-array-formation-through-concatenation/
 */
class Problem1640 {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        return dfs(arr, 0, pieces, new boolean[pieces.length]);
    }

    private boolean dfs(int[] arr, int i, int[][] pieces, boolean[] used) {
        if (i == arr.length) return true;
        for (int j = 0; j < pieces.length; j++) {
            if (used[j]) continue;
            int k = i;
            boolean ok = true;
            while (k < arr.length && k - i < pieces[j].length) {
                if (pieces[j][k - i] != arr[k]) {
                    ok = false;
                    break;
                }
                k++;
            }
            if (ok) {
                used[j] = true;
                if (dfs(arr, k, pieces, used)) return true;
                used[j] = false;
            }
        }
        return false;
    }
}
