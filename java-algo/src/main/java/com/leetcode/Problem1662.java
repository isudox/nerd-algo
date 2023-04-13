package com.leetcode;

/**
 * 1662. Check If Two String Arrays are Equivalent
 * https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
 */
public class Problem1662 {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        return concat(word1).equals(concat(word2));
    }

    private String concat(String[] words) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            sb.append(word);
        }
        return sb.toString();
    }
}
