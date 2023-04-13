package com.leetcode;

/**
 * 809. Expressive Words
 * https://leetcode.com/problems/expressive-words/
 */
public class Problem809 {
    public int expressiveWords(String s, String[] words) {
        int ans = 0;
        for (String word : words) {
            if (check(s, word)) {
                ans++;
            }
        }
        return ans;
    }

    private boolean check(String s, String word) {
        if (word.length() > s.length()) {
            return false;
        }
        int i = 0, j = 0;
        while (i < s.length() && j < word.length()) {
            if (s.charAt(i) != word.charAt(j)) {
                if (j == 0 || word.charAt(j - 1) != s.charAt(i)) {
                    return false;
                }
                int l = i, r = i;
                while (l >= 0 && s.charAt(l) == s.charAt(i)) {
                    l--;
                }
                while (r < s.length() && s.charAt(r) == s.charAt(i)) {
                    r++;
                }
                if (r - l - 1 < 3) {
                    return false;
                }
                i = r;
            } else {
                i++;
                j++;
            }
        }
        if (i >= s.length() && j >= word.length()) {
            return true;
        }
        if (i >= s.length()) {
            return false;
        }
        int l = i, r = i;
        while (l >= 0 && s.charAt(l) == s.charAt(i)) {
            l--;
        }
        while (r < s.length() && s.charAt(r) == s.charAt(i)) {
            r++;
        }
        return r - l - 1 >= 3 && r >= s.length();
    }
}
