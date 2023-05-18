package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1073. Adding Two Negabinary Numbers
 * https://leetcode.com/problems/adding-two-negabinary-numbers/
 */
public class Problem1073 {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        long num = toInt(arr1) + toInt(arr2);
        if (num == 0) {
            return new int[]{0};
        }
        List<Integer> list = new ArrayList<>();
        while (num != 0) {
            long a = num / -2, b = num % -2;
            if (b == -1) {
                b = 1;
                a++;
            }
            list.add((int) b);
            num = a;
        }
        int[] ans = new int[list.size()];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = list.get(list.size() - 1 - i);
        }
        return ans;
    }

    private long toInt(int[] arr) {
        long base = 1;
        long num = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            num += base * arr[i];
            base *= -2;
        }
        return num;
    }

    public static void main(String[] args) {
        Problem1073 p = new Problem1073();
        // [1,1,0,1,1,1]
        System.out.println(-13/-2);
        System.out.println(-13%-2);
        System.out.println(Arrays.toString(p.addNegabinary(new int[]{1, 0, 1, 1}, new int[]{1, 1, 0, 0})));
    }
}
