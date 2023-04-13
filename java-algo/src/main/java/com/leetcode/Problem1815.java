package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1815. Maximum Number of Groups Getting Fresh Donuts
 * https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
 */
public class Problem1815 {
    private static final int K_WIDTH = 5;
    private static final int K_WIDTH_MASK = (1 << K_WIDTH) - 1;

    public int maxHappyGroups(int batchSize, int[] groups) {
        int[] count = new int[batchSize];
        for (int group : groups) {
            count[group % batchSize]++;
        }
        Map<Long, Integer> memo = new HashMap<>();
        long start = 0;
        for (int i = batchSize - 1; i > 0; i--) {
            start = (start << K_WIDTH) | count[i];
        }
        return dfs(batchSize, start, memo) + count[0];
    }

    private int dfs(int batchSize, long mask, Map<Long, Integer> memo) {
        if (mask == 0) {
            return 0;
        }
        if (memo.containsKey(mask)) {
            return memo.get(mask);
        }
        long total = 0;
        for (int i = 1; i < batchSize; i++) {
            long amount = (mask >> ((i - 1) * K_WIDTH)) & K_WIDTH_MASK;
            total += amount * i;
        }
        int tmp = 0;
        for (int i = 1; i < batchSize; i++) {
            long amount = (mask >> ((i - 1) * K_WIDTH)) & K_WIDTH_MASK;
            if (amount > 0) {
                int ret = dfs(batchSize, mask - (1L << ((i - 1) * K_WIDTH)), memo);
                if ((total - i) % batchSize == 0) {
                    ret++;
                }
                tmp = Math.max(tmp, ret);
            }
        }
        memo.put(mask, tmp);
        return tmp;
    }
}
