package com.leetcode;

import java.util.Arrays;

/**
 * 1011. Capacity To Ship Packages Within D Days
 * https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
 *
 * A conveyor belt has packages that must be shipped from one port to another
 * within D days.
 *
 * The i^th package on the conveyor belt has a weight of weights[i]. Each day,
 * we load the ship with packages on the conveyor belt (in the order given by
 * weights). We may not load more weight than the maximum weight capacity of the
 * ship.
 *
 * Return the least weight capacity of the ship that will result in all the
 * packages on the conveyor belt being shipped within D days.
 *
 * Example 1:
 * Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
 * Output: 15
 * Explanation: A ship capacity of 15 is the minimum to ship all the packages in
 * 5 days like this:
 * 1st day: 1, 2, 3, 4, 5
 * 2nd day: 6, 7
 * 3rd day: 8
 * 4th day: 9
 * 5th day: 10
 *
 * Note that the cargo must be shipped in the order given, so using a ship of
 * capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
 * 7), (8), (9), (10) is not allowed.
 *
 * Example 2:
 * Input: weights = [3,2,2,4,1,4], D = 3
 * Output: 6
 * Explanation: A ship capacity of 6 is the minimum to ship all the packages in
 * 3 days like this:
 * 1st day: 3, 2
 * 2nd day: 2, 4
 * 3rd day: 1, 4
 *
 * Example 3:
 * Input: weights = [1,2,3,1,1], D = 4
 * Output: 3
 * Explanation:
 * 1st day: 1
 * 2nd day: 2
 * 3rd day: 3
 * 4th day: 1, 1
 *
 * Constraints:
 * 1 <= D <= weights.length <= 5 * 10^4
 * 1 <= weights[i] <= 500
 */
public class Problem1011 {
    public int shipWithinDays(int[] weights, int d) {
        int n = weights.length;
        int[] preSums = new int[n];
        int maxWeight = preSums[0] = weights[0];
        for (int i = 1; i < n; i++) {
            preSums[i] = preSums[i - 1] + weights[i];
            maxWeight = Math.max(maxWeight, weights[i]);
        }
        int lo = maxWeight, hi = preSums[n - 1], mid;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (helper(preSums, mid, n, d)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean helper(int[] array, int capacity, int n, int d) {
        int days = 1, limit = capacity;
        int i = 0;
        while (i < n) {
            i = Arrays.binarySearch(array, limit);
            if (i < 0) {
                i = -i - 1;
            }
            if (i < n) {
                if (array[i] > limit)
                    i--;
                limit = array[i] + capacity;
                i++;
                days++;
                if (days > d)
                    return false;
                if (days == d)
                    return array[array.length - 1] <= limit;
            }
        }
        return true;
    }

    public int shipWithinDays2(int[] weights, int d) {
        int lo = 0, hi = 0, mid;
        for (int weight : weights) {
            lo = Math.max(weight, lo);
            hi += weight;
        }
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (canShip(weights, mid, d))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }

    private boolean canShip(int[] weights, int capacity, int d) {
        int sum = 0;
        for (int weight : weights) {
            if (weight > capacity)
                return false;
            sum += weight;
            if (sum > capacity) {
                sum = weight;
                d--;
            }
            if (d <= 0)
                return false;
        }
        return true;
    }
}

