package com.leetcode;

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
