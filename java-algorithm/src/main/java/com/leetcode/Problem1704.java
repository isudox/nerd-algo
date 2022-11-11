package com.leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 1704. Determine if String Halves Are Alike
 * https://leetcode.com/problems/determine-if-string-halves-are-alike/
 */
public class Problem1704 {
    static Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

    public boolean halvesAreAlike(String s) {
        int i = 0, j = s.length() - 1;
        int d = 0;
        while (i < j) {
            if (vowels.contains(s.charAt(i++))) {
                d++;
            }
            if (vowels.contains(s.charAt(j--))) {
                d--;
            }
        }
        return d == 0;
    }
}
