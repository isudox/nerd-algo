package com.leetcode;

/**
 * 2027. Minimum Moves to Convert String
 * https://leetcode.com/problems/minimum-moves-to-convert-string/
 */
public class Problem2027 {
    public int minimumMoves(String s) {
        int ans = 0;
        int i = 0;
        while (i < s.length()) {
            while (i < s.length() && s.charAt(i) == 'O') {
                i++;
            }
            if (i < s.length()) {
                ans++;
                i += 3;
            }
        }
        return ans;
    }
}
