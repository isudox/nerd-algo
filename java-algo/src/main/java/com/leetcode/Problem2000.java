package com.leetcode;

/**
 * 2000. Reverse Prefix of Word
 * https://leetcode.com/problems/reverse-prefix-of-word/
 */
public class Problem2000 {
    public String reversePrefix(String word, char ch) {
        int i = 0;
        while (i < word.length()) {
            if (word.charAt(i) == ch) {
                break;
            }
            i++;
        }
        if (i == word.length()) {
            return word;
        }
        StringBuilder sb = new StringBuilder();
        for (int j = i; j >= 0; j--) {
            sb.append(word.charAt(j));
        }
        return sb.append(word.substring(i + 1)).toString();
    }
}
