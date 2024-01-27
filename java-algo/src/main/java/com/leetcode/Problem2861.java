package com.leetcode;

import java.util.List;

/**
 * https://leetcode.com/problems/maximum-number-of-alloys
 */
public class Problem2861 {
    public int maxNumberOfAlloys(int n, int k, int budget, List<List<Integer>> composition, List<Integer> stock, List<Integer> cost) {
        int lo = 1, hi = 200000000, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            boolean ok = false;
            for (int i = 0; i < k; i++) {
                long spend = 0L;
                for (int j = 0; j < n; j++) {
                    spend += Math.max((long) composition.get(i).get(j) * mid - stock.get(j), 0) * cost.get(j);
                }
                if (spend <= budget) {
                    ok = true;
                    break;
                }
            }
            if (ok) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
}
