package com.leetcode;

import java.util.Arrays;

/**
 * 826. Most Profit Assigning Work
 * https://leetcode.com/problems/most-profit-assigning-work
 */
public class Problem826 {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int ans = 0;
        int n = difficulty.length;
        int[][] store = new int[n][2];
        for (int i = 0; i < n; i++) {
            store[i] = new int[]{difficulty[i], profit[i]};
        }
        Arrays.sort(store, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        int[] max = new int[n];
        max[0] = store[0][1];
        for (int i = 1; i < n; i++) {
            max[i] = Math.max(max[i - 1], store[i][1]);
        }
        for (int w : worker) {
            int pick = helper(store, w);
            if (pick >= 0) {
                ans += max[pick];
            }
        }
        return ans;
    }

    // 找到最接近 limit store[i][0]，返回该 i 位置
    private int helper(int[][] store, int limit) {
        int lo = 0, hi = store.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (store[mid][0] == limit) {
                return mid;
            }
            if (store[mid][0] < limit) {
                if (mid + 1 == store.length || store[mid + 1][0] > limit) {
                    return mid;
                }
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi;
    }
}
