package com.leetcode;

public class JumpGameII {

    public int jump(int[] nums) {
        int size = nums.length;
        if (size < 2)
            return 0;
        int[] memo = new int[size];
        for (int i = 0; i < size; i++)
            memo[i] = size;
        try_jump(0, 0, nums, memo);
        return memo[size - 1];
    }

    private void try_jump(int i, int pre_steps, int[] nums, int[] memo) {
        if (i == nums.length - 1)
            return;
        for (int j = nums[i]; j >= 0; j--) {
            int k = Math.min(i + j, nums.length - 1);
            if (memo[k] < nums.length) {
                if (pre_steps + 1 < memo[k]) {
                    memo[k] = Math.min(pre_steps + 1, memo[k]);
                    try_jump(k, pre_steps + 1, nums, memo);
                }
            } else {
                memo[k] = pre_steps + 1;
                try_jump(k, pre_steps + 1, nums, memo);
            }
        }
    }
}
