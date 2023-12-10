package com.leetcode;

public class Problem2048 {
    public int nextBeautifulNumber(int n) {
        int x = n + 1;
        while (!check(x)) {
            x++;
        }
        return x;
    }

    private boolean check(int x) {
        int[] bits = new int[10];
        while (x > 0) {
            if (++bits[x % 10] > x % 10) {
                return false;
            }
            x /= 10;
        }
        for (int i = 0; i < 10; i++) {
            if (bits[i] > 0 && bits[i] != i) {
                return false;
            }
        }
        return true;
    }
}
