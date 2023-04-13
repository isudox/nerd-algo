package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 151. Reverse Words in a String
 * https://leetcode.com/problems/reverse-words-in-a-string/
 */
public class Problem151 {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        List<String> reversed = new ArrayList<>();
        for (int i = words.length - 1; i >= 0; i--) {
            if (words[i].length() > 0) {
                reversed.add(words[i]);
            }
        }
        return String.join(" ", reversed);
    }
}
