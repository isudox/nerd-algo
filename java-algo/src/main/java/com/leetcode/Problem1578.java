package com.leetcode;

/**
 * 1578. Minimum Time to Make Rope Colorful
 * https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
 */
public class Problem1578 {
    public int minCost(String colors, int[] neededTime) {
        int n = colors.length();
        int ans = 0;
        char preColor = '0';
        int preIndex = -1;
        for (int i = 0; i < n; i++) {
            char cur = colors.charAt(i);
            if (cur != preColor) {
                preColor = cur;
                preIndex = i;
            } else {
                int cost = neededTime[i];
                if (neededTime[i] > neededTime[preIndex]) {
                    cost = neededTime[preIndex];
                    preIndex = i;
                }
                ans += cost;
            }
        }
        return ans;
    }
}
