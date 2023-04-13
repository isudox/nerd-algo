package com.leetcode;

import java.util.Arrays;

/**
 * 1774. Closest Dessert Cost
 * https://leetcode.com/problems/closest-dessert-cost/
 */
public class Problem1774 {
    private int[] baseCosts;
    private int[] toppingCosts;
    int ans;

    public int closestCost(int[] baseCosts, int[] toppingCosts, int target) {
        this.ans = baseCosts[0];
        this.baseCosts = baseCosts;
        this.toppingCosts = toppingCosts;
        Arrays.sort(this.toppingCosts);
        for (int baseCost : baseCosts) {
            backtrack(0, baseCost, target);
        }
        return ans;
    }

    private void backtrack(int i, int costs, int target) {
        if (Math.abs(ans - target) < costs - target) {
            return;
        }
        if (Math.abs(ans - target) >= Math.abs(costs - target)) {
            if (Math.abs(ans - target) > Math.abs(costs - target)) {
                ans = costs;
            } else {
                ans = Math.min(ans, costs);
            }
        }
        if (i == this.toppingCosts.length) {
            return;
        }
        backtrack(i + 1, costs, target);
        backtrack(i + 1, costs + toppingCosts[i], target);
        backtrack(i + 1, costs + toppingCosts[i] * 2, target);
    }
}
