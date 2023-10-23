package com.leetcode;

/**
 * 2525. Categorize Box According to Criteria
 */
class Problem2525 {
    public String categorizeBox(int length, int width, int height, int mass) {
        boolean heavy = mass >= 100;
        boolean bulky = length >= 1e4 || width >= 1e4 || height >= 1e4 || ((long) length * width * height) >= (long) 1e9;
        if (bulky && heavy) return "Both";
        if (!bulky && !heavy) return "Neither";
        if (bulky) return "Bulky";
        else return "Heavy";
    }
}
