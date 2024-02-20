package com.leetcode;

public class Problem231 {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        if (n == 1) {
            return true;
        }
        while (n > 1) {
            if (n % 2 != 0) {
                return false;
            }
            n >>= 1;
        }
        return true;
    }
}
