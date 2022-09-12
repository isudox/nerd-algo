package com.leetcode;

import java.util.Arrays;

/**
 * 948. Bag of Tokens
 * https://leetcode.com/problems/bag-of-tokens/
 */
public class Problem948 {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int ans = 0;
        int score = 0;
        int i = 0, j = tokens.length - 1;
        while (i <= j && (power >= tokens[i] || score > 0)) {
            while (i <= j && power >= tokens[i]) {
                power -= tokens[i++];
                score++;
            }
            ans = Math.max(ans, score);
            if (i <= j && score > 0) {
                power += tokens[j--];
                score--;
            }
        }
        return ans;
    }
}
