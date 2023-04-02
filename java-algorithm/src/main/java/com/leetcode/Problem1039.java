package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
 */
public class Problem1039 {
    Map<Integer, Integer> memo = new HashMap<>();
    int n;

    public int minScoreTriangulation(int[] values) {
        this.n = values.length;
        return dfs(values, 0, n - 1);
    }

    private int dfs(int[] values, int i, int j) {
        if (i + 2 > j) {
            return 0;
        }
        if (i + 2 == j) {
            return values[i] * values[i + 1] * values[j];
        }
        int key = i * n + j;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        int ret = Integer.MAX_VALUE;
        for (int k = i + 1; k < j; k++) {
            ret = Math.min(ret, values[i] * values[k] * values[j] + dfs(values, i, k) + dfs(values, k, j));
        }
        memo.put(key, ret);
        return ret;
    }
}
