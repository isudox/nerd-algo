package com.leetcode;

import java.util.*;

/**
 * 1002. Find Common Characters
 * https://leetcode.com/problems/find-common-characters/
 */
public class Problem1002 {
    public List<String> commonChars(String[] words) {
        int[][] store = new int[words.length][26];
        for (int i = 0; i < words.length; i++) {
            for (char c : words[i].toCharArray()) {
                store[i][c - 'a']++;
            }
        }
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            int minCnt = store[0][i];
            for (int j = 1; j < words.length; j++) {
                minCnt = Math.min(minCnt, store[j][i]);
            }
            for (int j = 0; j < minCnt; j++) {
                ans.add(String.valueOf((char) ('a' + i)));
            }
        }
        return ans;
    }
}
