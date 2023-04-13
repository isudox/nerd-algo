package com.leetcode;

import java.util.Arrays;
import java.util.Random;

public class Problem384 {

    private final int[] nums;

    public Problem384(int[] nums) {
        this.nums = nums;
    }

    public int[] reset() {
        return this.nums;
    }

    public int[] shuffle() {
        int n = this.nums.length;
        int[] ret = new int[n];
        boolean[] used = new boolean[n];
        Arrays.fill(used, false);
        Random r = new Random();
        for (int i = 0; i < n; i++) {
            int idx = r.nextInt(n);
            while (used[idx]) {
                idx = r.nextInt(n);
            }
            used[idx] = true;
            ret[i] = this.nums[idx];
        }
        return ret;
    }
}
