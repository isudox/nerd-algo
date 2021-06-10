package com.leetcode;

/**
 * 518. Coin Change 2
 * https://leetcode.com/problems/coin-change-2/
 */
public class Problem518 {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins)
            for (int i = 1; i <= amount; i++)
                if (i >= coin) dp[i] += dp[i - coin];
        return dp[amount];
    }
}
