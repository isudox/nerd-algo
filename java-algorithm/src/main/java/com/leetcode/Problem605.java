package com.leetcode;

/**
 * 605. Can Place Flowers
 * https://leetcode.com/problems/can-place-flowers/
 */
public class Problem605 {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        for (int i = 0; i < flowerbed.length; i++) {
            if (n <= 0) {
                return true;
            }
            if (flowerbed.length - i < n) {
                return false;
            }
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                n--;
                if (n == 0) {
                    return true;
                }
                flowerbed[i] = 1;
            }
        }
        return n <= 0;
    }
}
