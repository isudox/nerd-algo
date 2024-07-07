package com.leetcode;

/**
 * 2582. Pass the Pillow
 * https://leetcode.com/problems/pass-the-pillow/
 */
public class Problem2582 {
    public int passThePillow(int n, int time) {
        int x = time / (n - 1), y = time % (n - 1);
        if (x % 2 == 0) {
            return y + 1;
        }
        return n - y;
    }
}
