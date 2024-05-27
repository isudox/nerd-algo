package com.leetcode;

import java.util.Arrays;

/**
 * 1255. Maximum Score Words Formed by Letters
 * https://leetcode.com/problems/maximum-score-words-formed-by-letters/
 */
public class Problem1255 {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int ans = 0;
        int n = words.length;
        int[] count = new int[26];
        for (char c : letters) {
            count[c - 'a']++;
        }
        int[] wordCount = new int[26]; // 统计子集 mask 所有单词的字母数目
        for (int mask = 1; mask < (1 << n); mask++) {
            Arrays.fill(wordCount, 0);
            for (int k = 0; k < n; k++) {
                if ((mask & (1 << k)) == 0) { // words[k] 不在子集 mask 中
                    continue;
                }
                for (int i = 0; i < words[k].length(); i++) {
                    char c = words[k].charAt(i);
                    wordCount[c - 'a']++;
                }
            }
            boolean ok = true; // 判断子集 mask 是否合法
            int sum = 0; // 保存子集 mask 的得分
            for (int i = 0; i < 26; i++) {
                sum += score[i] * wordCount[i];
                ok = ok && (wordCount[i] <= count[i]);
            }
            if (ok) {
                ans = Math.max(ans, sum);
            }
        }
        return ans;
    }
}
