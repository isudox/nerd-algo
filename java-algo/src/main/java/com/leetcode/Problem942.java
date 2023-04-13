package com.leetcode;

/**
 * 942. DI String Match
 * https://leetcode.com/problems/di-string-match/
 */
public class Problem942 {
    public int[] diStringMatch(String s) {
        int n = s.length();
        int[] ans = new int[n + 1];
        int minNum = 0, maxNum = n;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'I') {// pick current min num
                ans[i] = minNum++;
            } else {
                ans[i] = maxNum--;
            }
        }
        ans[n] = minNum;
        return ans;
    }
}
