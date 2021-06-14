package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1449. Form Largest Integer With Digits That Add up to Target
 * https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
 *
 * cost.length == 9
 * 1 <= cost[i] <= 5000
 * 1 <= target <= 5000
 */
public class Problem1449 {
    public String largestNumber(int[] cost, int target) {
        Map<Integer, String> memo = new HashMap<>();
        return dfs(cost, target, memo);
    }

    private String dfs(int[] cost, int target, Map<Integer, String> memo) {
        if (memo.containsKey(target))
            return memo.get(target);
        if (target == 0) return "";
        String ans = "0";
        for (int i = 0; i < cost.length; i++) {
            if (cost[i] <= target) {
                String ret = dfs(cost, target - cost[i], memo);
                if (!ret.equals("0")) {
                    ret = (i + 1) + ret;
                    if (compare(ret, ans) > 0) {
                        ans = ret;
                    }
                }
            }
        }
        memo.put(target, ans);
        return ans;
    }

    private int compare(String s1, String s2) {
        return s1.length() == s2.length() ? s1.compareTo(s2) : s1.length() - s2.length();
    }

    private int getSize(int[] cost, int target) {
        // dp[i][j]: cost 前 i 个数，组成 j 的最大元素个数
        int[][] dp = new int[cost.length + 1][target + 1];
        for (int i = 1; i <= cost.length; i++) {
            for (int j = 1; j <= target; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j == cost[i - 1])
                    dp[i][j] = Math.max(dp[i][j], 1);
                if (j > cost[i - 1] && dp[i][j - cost[i - 1]] != 0)
                    dp[i][j] = Math.max(dp[i][j], dp[i][j - cost[i - 1]] + 1);
            }
        }
        return dp[cost.length][target];
    }

    public static void main(String[] args) {
        Problem1449 sol = new Problem1449();
        System.out.println("" + sol.getSize(new int[]{4, 3, 2, 5, 6, 7, 2, 5, 5}, 9));
        System.out.println("" + sol.getSize(new int[]{7, 6, 5, 5, 5, 6, 8, 7, 8}, 12));
        System.out.println("" + sol.getSize(new int[]{2,4,6,2,4,6,4,4,4}, 5));
        System.out.println("" + sol.getSize(new int[]{6,10,15,40,40,40,40,40,40}, 47));
        System.out.println("\n");
        System.out.println("" + sol.largestNumber(new int[]{5,6,7,3,4,6,7,4,8}, 29));
        System.out.println("" + sol.largestNumber(new int[]{5, 4, 4, 5, 5, 5, 5, 5, 5}, 19));
        System.out.println("" + sol.largestNumber(new int[]{6,10,15,40,40,40,40,40,40}, 47));
    }
}
