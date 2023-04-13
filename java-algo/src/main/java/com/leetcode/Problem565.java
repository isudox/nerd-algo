package com.leetcode;

/**
 * 565. Array Nesting
 * https://leetcode.com/problems/array-nesting/
 */
public class Problem565 {
    public int arrayNesting(int[] nums) {
        boolean[] seen = new boolean[nums.length];
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = i;
            int cnt = 0;
            while (!seen[nums[x]]) {
                seen[nums[x]] = true;
                cnt++;
                x = nums[x];
            }
            if (cnt > ans) {
                ans = cnt;
            }
        }
        return ans;
    }
}
