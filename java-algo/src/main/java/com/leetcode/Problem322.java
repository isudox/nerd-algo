package com.leetcode;

import java.util.*;

/**
 * 322. Coin Change
 * https://leetcode.com/problems/coin-change/
 */
public class Problem322 {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }
        Arrays.sort(coins);
        Set<Integer> set = new HashSet<>();
        for (int coin : coins) {
            set.add(coin);
        }
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            if (set.contains(i)) {
                dp[i] = 1;
                continue;
            }
            int cnt = Integer.MAX_VALUE;
            for (int coin : coins) {
                if (coin > i) {
                    break;
                }
                int tmp = dp[i - coin];
                if (tmp != -1) {
                    cnt = Math.min(cnt, tmp);
                }
            }
            dp[i] = cnt == Integer.MAX_VALUE ? -1 : cnt + 1;
        }
        return dp[amount];
    }

    public int coinChange2(int[] coins, int amount) {
        Arrays.sort(coins);
        int ans = dfs(coins, amount, new int[amount + 1]);
        return ans < Integer.MAX_VALUE ? ans : -1;
    }

    private int dfs(int[] coins, int need, int[] memo) {
        if (need == 0) {
            return 0;
        }
        if (memo[need] > 0) {
            return memo[need];
        }
        int ret = Integer.MAX_VALUE;
        for (int coin : coins) {
            if (coin > need) {
                break;
            }
            int res = dfs(coins, need - coin, memo);
            if (res < Integer.MAX_VALUE) {
                ret = Math.min(ret, dfs(coins, need - coin, memo) + 1);
            }
        }
        return memo[need] = ret;
    }
}
