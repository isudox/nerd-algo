package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 464. Can I Win
 * https://leetcode.com/problems/can-i-win/
 */
public class Problem464 {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        Map<Integer, Boolean> memo = new HashMap<>();
        if ((1 + maxChoosableInteger) * (maxChoosableInteger) / 2 < desiredTotal) {
            return false;
        }
        return dfs(maxChoosableInteger, 0, desiredTotal, 0, memo);
    }

    private boolean dfs(int max, int used, int target, int cur, Map<Integer, Boolean> memo) {
        if (memo.containsKey(used)) {
            return memo.get(used);
        }
        boolean ret = false;
        for (int i = 0; i < max; i++) {
            if (((used >> i) & 1) == 0) {
                if (i + 1 + cur >= target) {
                    ret = true;
                    break;
                }
                if (!dfs(max, used | (1 << i), target, cur + i + 1, memo)) {
                    ret = true;
                    break;
                }
            }
        }
        memo.put(used, ret);
        return memo.get(used);
    }
}
