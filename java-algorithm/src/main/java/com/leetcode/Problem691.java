package com.leetcode;

import java.util.Arrays;

/**
 * 691. Stickers to Spell Word
 * https://leetcode.com/problems/stickers-to-spell-word/
 */
public class Problem691 {
    private String[] stickers;
    private String target;
    private int[] memo;

    public int minStickers(String[] stickers, String target) {
        this.stickers = stickers;
        this.target = target;
        int n = target.length();
        int limit = 1 << n;
        this.memo = new int[limit];
        Arrays.fill(this.memo, -1);
        int ans = dfs(0);
        return ans < Integer.MAX_VALUE ? ans : -1;
    }

    private int dfs(int state) {
        int n = target.length();
        if (state == ((1 << n) - 1)) {
            return 0;
        }
        if (memo[state] != -1) {
            return memo[state];
        }
        int ret = Integer.MAX_VALUE;
        for (String s : stickers) {
            int nstate = state;
            for (char ch : s.toCharArray()) {
                for (int i = 0; i < n; i++) {
                    if (target.charAt(i) == ch && ((nstate >> i) & 1) == 0) {
                        nstate |= (1 << i);
                        break;
                    }
                }
            }
            if (nstate != state) {
                int tmp = dfs(nstate);
                ret = Math.min(ret, tmp == Integer.MAX_VALUE ? tmp : tmp + 1);
            }
        }
        return memo[state] = ret;
    }
}
