package com.leetcode;

import java.util.*;

/**
 * 526. Beautiful Arrangement
 * https://leetcode.com/problems/beautiful-arrangement/
 */
public class Problem526 {
    public int countArrangement(int n) {
        return dfs(1, n, 0, new HashMap<>());
    }

    private int dfs(int pos, int n, int bits, Map<Integer, Integer> memo) {
        if (pos > n) return 1;
        if (memo.containsKey(bits)) return memo.get(bits);
        int ret = 0;
        for (int num = 1; num <= n; num++) {
            int bit = (bits >> num) & 1;
            if (bit == 0 && (num % pos == 0 || pos % num == 0))
                ret += dfs(pos + 1, n, bits + (1 << num), memo);
        }
        memo.put(bits, ret);
        return ret;
    }
}
