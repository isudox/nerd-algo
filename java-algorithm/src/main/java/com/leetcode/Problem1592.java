package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1592. Rearrange Spaces Between Words
 */
public class Problem1592 {
    public String reorderSpaces(String text) {
        int letters = 0;
        String[] splits = text.split(" ");
        List<String> words = new ArrayList<>();
        for (String split : splits) {
            if (split.length() > 0) {
                letters += split.length();
                words.add(split);
            }
        }
        int spaces = text.length() - letters;
        if (words.size() == 1) return words.get(0) + " ".repeat(spaces);
        int avg = spaces / (words.size() - 1);
        int rem = spaces % (words.size() - 1);
        StringBuilder sb = new StringBuilder(words.get(0));
        for (int i = 1; i < words.size(); i++) {
            sb.append(" ".repeat(avg)).append(words.get(i));
        }
        if (rem > 0) sb.append(" ".repeat(rem));
        return sb.toString();
    }
}
