package com.leetcode;

/**
 * 1518. Water Bottles
 * https://leetcode.com/problems/water-bottles/
 */
public class Problem1518 {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        while (numBottles >= numExchange) {
            int x = numBottles / numExchange;
            int y = numBottles % numExchange;
            numBottles = x + y;
            ans += x;
        }
        return ans;
    }
}
