package com.leetcode;

import java.util.*;

/**
 * 309. Best Time to Buy and Sell Stock with Cooldown
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
 * <p>
 * Say you have an array for which the ith element is the price of a given stock
 * on day i.
 * <p>
 * Design an algorithm to find the maximum profit. You may complete as many
 * transactions as you like
 * (ie, buy one and sell one share of the stock multiple times)
 * with the following restrictions:
 * <p>
 * You may not engage in multiple transactions at the same time
 * (ie, you must sell the stock before you buy again).
 * After you sell your stock, you cannot buy stock on next day.
 * (ie, cooldown 1 day)
 * <p>
 * Example:
 * <p>
 * Input: [1,2,3,0,2]
 * Output: 3
 * Explanation: transactions = [buy, sell, cooldown, buy, sell]
 */
public class Problem350 {

    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length)
            return intersect(nums2, nums1);
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums1) {
            if (count.containsKey(num))
                count.put(num, count.get(num) + 1);
            else
                count.put(num, 1);
        }
        List<Integer> list = new ArrayList<>();
        for (int num : nums2) {
            if (count.containsKey(num) && count.get(num) > 0) {
                list.add(num);
                count.put(num, count.get(num) - 1);
            }
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }

    public int[] intersect1(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0, j = 0;
        List<Integer> list = new ArrayList<>();
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                list.add(nums1[i]);
                i++;
                j++;
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}
