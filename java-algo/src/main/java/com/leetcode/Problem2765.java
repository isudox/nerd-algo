package com.leetcode;

public class Problem2765 {
    public int alternatingSubarray(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int j = i + 1;
            while (j < nums.length && nums[j] == nums[j - 1] + ((j - i) % 2 == 1 ? 1 : -1)) {
                j++;
            }
            ans = Math.max(ans, j - i);
        }
        return ans > 1 ? ans : -1;
    }
}
