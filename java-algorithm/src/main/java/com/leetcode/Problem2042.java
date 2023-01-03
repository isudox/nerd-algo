package com.leetcode;

/**
 * 2042. Check if Numbers Are Ascending in a Sentence
 * https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
 */
public class Problem2042 {
    public boolean areNumbersAscending(String s) {
        String[] words = s.split(" ");
        int pre = -1;
        for (String word : words) {
            if (isNum(word)) {
                int num = Integer.parseInt(word);
                if (num <= pre) {
                    return false;
                }
                pre = num;
            }
        }
        return true;
    }

    private boolean isNum(String word) {
        int d = word.charAt(0) - '0';
        return 0 <= d && d <= 9;
    }
}
