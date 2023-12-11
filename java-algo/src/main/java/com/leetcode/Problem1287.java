package com.leetcode;

/**
 * 1287. Element Appearing More Than 25% In Sorted Array
 * https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array
 */
public class Problem1287 {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length / 4;
        if (n * 4 <= arr.length) {
            n++;
        }
        int num = arr[0];
        int cnt = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == num) {
                cnt++;
            } else {
                num = arr[i];
                cnt = 1;
            }
            if (cnt == n) {
                return num;
            }
        }
        return num;
    }
}
