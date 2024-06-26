package com.leetcode;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * 648. Replace Words
 * https://leetcode.com/problems/replace-words/
 */
public class Problem648 {
    public String replaceWords(List<String> dictionary, String sentence) {
        dictionary.sort(Comparator.comparingInt(String::length));
        String[] words = sentence.split(" ");
        List<String> ans = new ArrayList<>();
        for (String word : words) {
            boolean flag = false;
            for (String d : dictionary) {
                if (word.startsWith(d)) {
                    ans.add(d);
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                ans.add(word);
            }
        }
        return String.join(" ", ans);
    }
}
