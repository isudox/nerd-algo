package com.leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 2465. Number of Distinct Averages
 * https://leetcode.com/problems/number-of-distinct-averages/
 */
public class Problem2465 {
    public int distinctAverages(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;
        Set<Float> seen = new HashSet<>();
        int i = 0, j = nums.length - 1;
        while (i < j) {
            float x = (float) (nums[i++] + nums[j--]) / 2;
            if (!seen.contains(x)) {
                seen.add(x);
                ans++;
            }
        }
        return ans;
    }
}
