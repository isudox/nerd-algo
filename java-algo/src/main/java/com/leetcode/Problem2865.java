package com.leetcode;

import java.util.List;

/**
 * 2865. Beautiful Towers I
 * https://leetcode.com/problems/beautiful-towers-i/
 */
public class Problem2865 {
    public long maximumSumOfHeights(List<Integer> maxHeights) {
        int n = maxHeights.size();
        long ans = 0L;
        for (int i = 0; i < n; i++) {
            long sum = maxHeights.get(i);
            long curMax = maxHeights.get(i);
            for (int j = i - 1; j >= 0; j--) {
                curMax = Math.min(curMax, maxHeights.get(j));
                sum += curMax;
            }
            curMax = maxHeights.get(i);
            for (int k = i + 1; k < n; k++) {
                curMax = Math.min(curMax, maxHeights.get(k));
                sum += curMax;
            }
            ans = Math.max(ans, sum);
        }
        return ans;
    }
}
