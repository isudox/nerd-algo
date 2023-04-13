package com.leetcode;

/**
 * 902. Numbers At Most N Given Digit Set
 * https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
 */
public class Problem902 {

    public int atMostNGivenDigitSet(String[] digits, int n) {
        int ans = 0;
        int cnt = digits.length;
        String nn = "" + n;
        for (int i = 1; i < nn.length(); i++) {
            ans += Math.pow(cnt, i);
        }
        ans += dfs(digits, nn, 0, 0);
        return ans;
    }

    private int dfs(String[] digits, String nn, int pos, int flag) {
        if (pos == nn.length()) {
            return 1;
        }
        if (flag == 1) {// is less than n
            return (int) Math.pow(digits.length, nn.length() - pos);
        }
        int ret = 0;
        for (String num : digits) {
            if (num.charAt(0) > nn.charAt(pos)) {
                break;
            }
            if (num.charAt(0) == nn.charAt(pos)) {
                ret += dfs(digits, nn, pos + 1, 0);
            } else {
                ret += dfs(digits, nn, pos + 1, 1);
            }
        }
        return ret;
    }
}
