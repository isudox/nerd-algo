package com.leetcode;

/**
 * 838. Push Dominoes
 * https://leetcode.com/problems/push-dominoes/
 */
public class Problem838 {
    public String pushDominoes(String dominoes) {
        char[] s  = dominoes.toCharArray();
        int n = s.length;
        int i = 0;
        char left = 'L';
        while (i < n) {
            int j = i;
            while (j < n && s[j] == '.') {
                j++;
            }
            char right = j < n ? s[j] : 'R';
            if (left == right) {
                while (i < j) {
                    s[i++] = right;
                }
            } else if (left == 'R' && right == 'L') {
                int k = j - 1;
                while (i < k) {
                    s[i++] = 'R';
                    s[k--] = 'L';
                }
            }
            left = right;
            i = j + 1;
        }
        return new String(s);
    }
}
