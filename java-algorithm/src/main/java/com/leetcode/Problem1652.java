package com.leetcode;

/**
 * 1652. Defuse the Bomb
 * https://leetcode.com/problems/defuse-the-bomb/
 */
public class Problem1652 {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] ans = new int[n];
        if (k == 0) return ans;
        int step = k > 0 ? 1 : -1;
        int win = 0, pos = 0;
        for (int i = 0; i < Math.abs(k); i++) {
            pos = (pos + step + n) % n;
            win += code[pos];
        }
        ans[0] = win;
        for (int i = 1; i < n; i++) {
            if (step == 1)
                win += code[(i + k) % n] - code[i];
            else
                win += code[i - 1] - code[(i + k + n - 1) % n];
            ans[i] = win;
        }
        return ans;
    }
}
