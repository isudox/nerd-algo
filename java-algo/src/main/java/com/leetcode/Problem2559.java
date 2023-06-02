package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 2559. Count Vowel Strings in Ranges
 * https://leetcode.com/problems/count-vowel-strings-in-ranges/
 */
public class Problem2559 {
    public int[] vowelStrings(String[] words, int[][] queries) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        boolean[] marks = new boolean[words.length];
        for (int i = 0; i < words.length; i++) {
            marks[i] = vowels.contains(words[i].charAt(0)) && vowels.contains(words[i].charAt(words[i].length() - 1));
        }
        int[] preSum = new int[words.length + 1];
        for (int i = 1; i <= words.length; i++) {
            preSum[i] = preSum[i - 1] + (marks[i - 1] ? 1 : 0);
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            ans[i] = preSum[queries[i][1] + 1] - preSum[queries[i][0]];
        }
        return ans;
    }
}
