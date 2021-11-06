package com.leetcode;

/**
 * 441. Arranging Coins
 * https://leetcode.com/problems/arranging-coins/
 * 1 <= n <= 2^31-1
 */
public class Problem441 {
    public int arrangeCoins(int n) {
        int level = 1;
        while (n >= level) {
            n -= level;
            level++;
        }
        return level - 1;
    }

    public int arrangeCoins2(int n) {
        // (x+1) * x / 2 = n
        int l = 1, r = n;
        while (l < r) {
            int mid = l + (r - l + 1) / 2;
            long cur = (long) (mid + 1) * mid / 2;
            if (cur == n) {
                return mid;
            }
            if (cur < n) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }

    public static void main(String[] args) {
        System.out.println(new Problem441().arrangeCoins2(5));
    }
}
