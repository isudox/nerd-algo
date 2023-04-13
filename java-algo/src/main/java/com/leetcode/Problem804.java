package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 804. Unique Morse Code Words
 * https://leetcode.com/problems/unique-morse-code-words/
 */
public class Problem804 {
    public int uniqueMorseRepresentations(String[] words) {
        String[] codes = new String[]{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        Set<String> set = new HashSet<>();
        for (String word : words) {
            StringBuffer sb = new StringBuffer();
            for (char ch : word.toCharArray()) {
                sb.append(codes[ch - 'a']);
            }
            String tmp = sb.toString();
            set.add(tmp);
        }
        return set.size();
    }
}
