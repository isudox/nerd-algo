package com.leetcode;

/**
 * 667. Beautiful Arrangement II
 * https://leetcode.com/problems/beautiful-arrangement-ii/
 */
public class Problem667 {
    public int[] constructArray(int n, int k) {
        int[] ans = new int[n];
        boolean[] used = new boolean[n + 1];
        ans[0] = 1;
        used[1] = true;
        // 先用 [1, k+1] 构成 k 个整数差
        for (int i = 1; i < k + 1; i++) {
            ans[i] = ans[i - 1] + k - (i - 1);
            if (ans[i] > k + 1 || used[ans[i]])
                ans[i] = ans[i - 1] - k + (i - 1);
            used[ans[i]] = true;
        }
        for (int i = k + 1; i < n; i++) {
            ans[i] = i + 1;
        }
        return ans;
    }
}
