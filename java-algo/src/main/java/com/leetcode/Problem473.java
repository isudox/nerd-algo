package com.leetcode;

import java.util.Arrays;

/**
 * 473. Matchsticks to Square
 * https://leetcode.com/problems/matchsticks-to-square/
 */
public class Problem473 {
    public boolean makesquare(int[] matchsticks) {
        int total = 0;
        for (int m : matchsticks) {
            total += m;
        }
        if (total % 4 != 0) {
            return false;
        }
        int edge = total / 4;
        Arrays.sort(matchsticks);
        if (matchsticks[matchsticks.length - 1] > edge) {
            return false;
        }
        return dfs(matchsticks, 0, new int[4], edge);
    }

    private boolean dfs(int[] matchsticks, int i, int[] groups, int edge) {
        if (i == matchsticks.length) {
            return true;
        }
        for (int x = 0; x < 4; x++) {
            if (groups[x] + matchsticks[i] > edge) {
                return false;
            }
            groups[x] += matchsticks[i];
            if (dfs(matchsticks, i + 1, groups, edge)) {
                return true;
            }
            groups[x] -= matchsticks[i];
        }
        return false;
    }
}
