package com.leetcode;

/**
 * 520. Detect Capital
 * https://leetcode.com/problems/detect-capital/
 */
public class Problem520 {
    public boolean detectCapitalUse(String word) {
        if (word.length() == 1) {
            return true;
        }
        boolean firstCapital = isCapital(word.charAt(0));
        boolean secondCapital = isCapital(word.charAt(1));
        if (!firstCapital && secondCapital) {
            return false;
        }
        boolean allCapital = firstCapital && secondCapital;
        for (int i = 2; i < word.length(); i++) {
            boolean curCapital = isCapital(word.charAt(i));
            if (allCapital ^ curCapital) {
                return false;
            }
        }
        return true;
    }

    private boolean isCapital(char c) {
        int d = c - 'A';
        return 0 <= d && d < 26;
    }
}
