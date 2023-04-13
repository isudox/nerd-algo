package com.leetcode;

/**
 * 567. Permutation in String
 * https://leetcode.com/problems/permutation-in-string/
 */
public class Problem567 {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) return false;
        int[] counter1 = new int[26];
        for (char c : s1.toCharArray()) {
            counter1[c - 'a']++;
        }
        int[] counter2 = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            counter2[s2.charAt(i) - 'a']++;
        }
        if (compare(counter1, counter2)) return true;
        for (int i = 1; i <= n2 - n1; i++) {
            counter2[s2.charAt(i - 1) - 'a']--;
            counter2[s2.charAt(i + n1 - 1) - 'a']++;
            if (compare(counter1, counter2)) return true;
        }
        return false;
    }

    private boolean compare(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
}
