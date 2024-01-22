package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem2788 {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> ans = new ArrayList<>();
        for (String word : words) {
            ans.addAll(helper(word, separator));
        }
        return ans;
    }

    private List<String> helper(String word, char separator) {
        List<String> ret = new ArrayList<>();
        StringBuilder cur = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == separator) {
                if (!cur.isEmpty()) {
                    ret.add(cur.toString());
                    cur = new StringBuilder();
                }
            } else {
                cur.append(word.charAt(i));
            }
        }
        if (!cur.isEmpty()) {
            ret.add(cur.toString());
        }
        return ret;
    }
}
