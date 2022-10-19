package com.leetcode;

public class Problem1832 {
    public boolean checkIfPangram(String sentence) {
        if (sentence.length() < 26) {
            return false;
        }
        int[] cnt = new int[26];
        for (int i = 0; i < sentence.length(); i++) {
            cnt[sentence.charAt(i) - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) {
                return false;
            }
        }
        return true;
    }
}
