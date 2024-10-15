package com.leetcode;

/**
 * 2938. Separate Black and White Balls
 * https://leetcode.com/problems/separate-black-and-white-balls/
 */
public class Problem2938 {
    public long minimumSteps(String s) {
        long ans = 0;
        int x = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '0') {
                ans += i - (x++);
            }
        }
        return ans;
    }
}
