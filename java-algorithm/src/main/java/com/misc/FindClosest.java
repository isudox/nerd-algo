package com.misc;

/**
 * https://leetcode.cn/problems/find-closest-lcci/
 */
public class FindClosest {
    public int findClosest(String[] words, String word1, String word2) {
        int[] pre = new int[]{-1, -1};
        int ans = words.length;
        for (int i = 0; i < words.length; i++) {
            if (!words[i].equals(word1) && !words[i].equals(word2)) {
                continue;
            }
            int pick = words[i].equals(word1) ? 0 : 1;
            if (pre[1 - pick] >= 0) {
                if (i - pre[1 - pick] < ans) {
                    ans = i - pre[1 - pick];
                }
            }
            pre[pick] = i;
        }
        return ans;
    }
}
