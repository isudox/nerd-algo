package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 819. Most Common Word
 * https://leetcode-cn.com/problems/most-common-word/
 */
public class Problem819 {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> set = new HashSet<>();
        for (String b : banned) {
            set.add(b.toLowerCase());
        }
        String lowerParagraph = paragraph.toLowerCase();
        StringBuilder sb = new StringBuilder();
        for (char ch : lowerParagraph.toCharArray()) {
            if (ch == '!' || ch == '?' || ch == '\'' || ch == ',' || ch == ';' || ch == '.') {
                sb.append(' ');
            } else {
                sb.append(ch);
            }
        }
        String[] words = sb.toString().split(" ");
        if (words.length == 0) {
            return "";
        }
        String ans = "";
        int cnt = 0;
        Map<String, Integer> counter = new HashMap<>();
        for (String word : words) {
            if (word.length() == 0) {
                continue;
            }
            if (set.contains(word)) {
                continue;
            }
            counter.put(word, counter.getOrDefault(word, 0) + 1);
            if (counter.get(word) > cnt) {
                cnt = counter.get(word);
                ans = word;
            }
        }
        return ans;
    }
}
