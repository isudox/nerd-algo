package com.leetcode;

import java.util.Arrays;

/**
 * 611. Valid Triangle Number
 * https://leetcode.com/problems/valid-triangle-number/
 */
public class Problem611 {
    public int triangleNumber(int[] nums) {
        int n = nums.length;
        if (n < 3) return 0;
        int ans = 0;
        Arrays.sort(nums);
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] + nums[j] > nums[k])
                        ans++;
                    else
                        break;
                }
            }
        }
        return ans;
    }
}
