package com.leetcode;

public class Problem169 {
    public int majorityElement(int[] nums) {
        int cnt = 0;
        int ans = 0;
        for (int num : nums) {
            if (cnt == 0) {
                ans = num;
            }
            if (num == ans) {
                cnt++;
            } else {
                cnt--;
            }
        }
        return ans;
    }
}
