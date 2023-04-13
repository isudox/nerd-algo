package com.leetcode;

import java.util.Arrays;

/**
 * 927. Three Equal Parts
 * https://leetcode.cn/problems/three-equal-parts/
 */
public class Problem927 {
    public int[] threeEqualParts(int[] arr) {
        int n = arr.length;
        int cnt1 = 0;
        for (int num : arr) {
            cnt1 += num;
        }
        if (cnt1 == 0) {
            return new int[]{0, n - 1};
        }
        if (cnt1 % 3 != 0) {
            return new int[]{-1, -1};
        }
        int avg1 = cnt1 / 3;
        int i = 0, j = 0, k = 0, cur = 0;
        for (int x = 0; x < n; x++) {
            if (arr[x] == 1) {
                if (cur == 0) {
                    i = x;
                } else if (cur == avg1) {
                    j = x;
                } else if (cur == 2 * avg1) {
                    k = x;
                }
                cur++;
            }
        }
        int len = n - k;
        if (i + len <= j && j + len <= k) {
            int x = 0;
            while (k + x < n) {
                if (arr[i + x] != arr[j + x] || arr[i + x] != arr[k + x]) {
                    return new int[]{-1, -1};
                }
                x++;
            }
            return new int[]{i + len - 1, j + len};
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        Problem927 p = new Problem927();
        System.out.println(Arrays.toString(p.threeEqualParts(new int[]{0, 0, 0, 0, 0}))); //1,4
        System.out.println(Arrays.toString(p.threeEqualParts(new int[]{0, 1, 0, 1, 1}))); //1,4
        System.out.println(Arrays.toString(p.threeEqualParts(new int[]{1, 0, 1, 0, 1}))); // 0,3
        System.out.println(Arrays.toString(p.threeEqualParts(new int[]{1, 1, 0, 1, 1})));//-1,-1
        System.out.println(Arrays.toString(p.threeEqualParts(new int[]{1, 1, 0, 0, 1})));//0,2
    }
}
