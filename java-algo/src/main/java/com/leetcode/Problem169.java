package com.leetcode;

/**
 * https://leetcode.com/problems/majority-elemen
 */
public class Problem169 {
    public int majorityElement(int[] nums) {
        int cnt = 0, ans = 0;
        for (int num : nums) {
            if (cnt == 0) {
                ans = num;
            }
            cnt += num == ans ? 1 : -1;
        }
        return ans;
    }
}
