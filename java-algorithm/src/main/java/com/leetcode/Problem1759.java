package com.leetcode;

/**
 * 1759. Count Number of Homogenous Substrings
 * https://leetcode.com/problems/count-number-of-homogenous-substrings/
 */
public class Problem1759 {
    public int countHomogenous(String s) {
        long ans = 0L;
        long cnt = 0L;
        char pre = '0';
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (cur == pre) {
                cnt++;
            } else {
                pre = cur;
                ans = (ans + (cnt * (cnt + 1) / 2));
                cnt = 1;
            }
        }
        return (int) ((ans + (cnt * (cnt + 1) / 2)) % 1000000007);
    }
}
