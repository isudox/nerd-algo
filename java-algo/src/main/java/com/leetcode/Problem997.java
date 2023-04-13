package com.leetcode;

/**
 * 997. Find the Town Judge
 * https://leetcode.com/problems/find-the-town-judge/
 */
class Problem997 {
    public int findJudge(int n, int[][] trust) {
        int[] store = new int[n + 1];
        for (int[] t : trust) {
            store[t[1]] += t[0];
            store[t[0]] -= t[1];
        }
        int total = n * (1 + n) / 2;
        for (int i = 1; i <= n; i++) {
            if (store[i] + i == total)
                return i;
        }
        return -1;
    }
}
