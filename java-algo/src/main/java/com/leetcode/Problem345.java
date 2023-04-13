package com.leetcode;

/**
 * 345. Reverse Vowels of a String
 * https://leetcode.com/problems/reverse-vowels-of-a-string/
 */
public class Problem345 {
    public String reverseVowels(String s) {
        char[] cs = s.toCharArray();
        int i = 0, j = cs.length - 1;
        while (i < j) {
            while (i < j && isVowel(cs[i])) {
                i++;
            }
            while (i < j && isVowel(cs[j])) {
                j--;
            }
            if (i < j) {
                char tmp = cs[i];
                cs[i] = cs[j];
                cs[j] = tmp;
                i++;
                j--;
            }
        }
        return new String(cs);
    }

    private boolean isVowel(char c) {
        return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U';
    }
}
