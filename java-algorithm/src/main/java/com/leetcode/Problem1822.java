package com.leetcode;

/**
 * 1822. Sign of the Product of an Array
 * https://leetcode.com/problems/sign-of-the-product-of-an-array/
 */
public class Problem1822 {
    public int arraySign(int[] nums) {
        int negs = 0;
        for (int num : nums) {
            if (num == 0) {
                return 0;
            }
            if (num < 0) {
                negs++;
            }
        }
        return negs % 2 == 0 ? 1 : -1;
    }
}
