package com.leetcode;

/**
 * 481. Magical String
 * https://leetcode.com/problems/magical-string/
 */
public class Problem481 {
    public int magicalString(int n) {
        if (n == 1) {
            return 1;
        }
        int[] nums = new int[n];
        nums[0] = 1;
        nums[1] = 2;
        int i = 1, j = 1;
        int num = 1;
        int ans = 1;
        while (i < n) {
            num = 3 - num;
            int cnt = Math.min(nums[j++], n - i);
            if (num == 1) {
                ans += cnt;
            }
            for (int k = 0; k < cnt; k++) {
                nums[i++] = num;
            }
        }
        return ans;
    }
}
