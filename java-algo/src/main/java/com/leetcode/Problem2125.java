package com.leetcode;

/**
 * 2125. Number of Laser Beams in a Bank
 * https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
 */
public class Problem2125 {
    public int numberOfBeams(String[] bank) {
        int ans = 0;
        int pre = 0;
        for (String line : bank) {
            int cnt = count(line);
            if (cnt != 0) {
                ans += pre * cnt;
                pre = cnt;
            }
        }
        return ans;
    }

    private int count(String line) {
        int cnt = 0;
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '1') {
                cnt++;
            }
        }
        return cnt;
    }
}
