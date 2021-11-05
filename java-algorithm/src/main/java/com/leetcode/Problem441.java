package com.leetcode;

/**
 * 441. Arranging Coins
 * https://leetcode.com/problems/arranging-coins/
 * 1 <= n <= 2^31-1
 */
public class Problem441 {
    public int arrangeCoins(int n) {
        // (1+x)*x/2 == n
        int level = 1;
        while (n >= level) {
            n -= level;
            level++;
        }
        return level - 1;
    }

    public static void main(String[] args) {
        System.out.println(new Problem441().arrangeCoins(1));
    }
}
