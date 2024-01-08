package com.leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/**
 * 446. Arithmetic Slices II - Subsequence
 * https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
 */
public class Problem446 {
    public int numberOfArithmeticSlices(int[] nums) {
        int ans = 0;
        Map<Tuple, Integer> memo = new HashMap<>();
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                ans += dfs(nums, j, (long) nums[j] - (long) nums[i], memo);
            }
        }
        return ans;
    }

    private int dfs(int[] nums, int pos, long diff, Map<Tuple, Integer> memo) {
        Tuple key = new Tuple(pos, diff);
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        if (pos == nums.length - 1) {// find one num only.
            return 0;
        }
        int ret = 0;
        for (int i = pos + 1; i < nums.length; i++) {
            if ((long) nums[i] - (long) nums[pos] == diff) {// find two nums at least.
                ret += dfs(nums, i, diff, memo) + 1;
            }
        }
        memo.put(key, ret);
        return ret;
    }

    static class Tuple {
        int pos;
        long diff;

        public Tuple(int pos, long diff) {
            this.pos = pos;
            this.diff = diff;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Tuple tuple = (Tuple) o;
            return pos == tuple.pos && diff == tuple.diff;
        }

        @Override
        public int hashCode() {
            return Objects.hash(pos, diff);
        }
    }
}
