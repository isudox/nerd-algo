package com.leetcode;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1073. Adding Two Negabinary Numbers
 * https://leetcode.com/problems/adding-two-negabinary-numbers/
 */
public class Problem1073 {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        List<Integer> list = new ArrayList<>();
        int pre = 0;
        int i = arr1.length - 1, j = arr2.length - 1;
        while (i >= 0 || j >= 0 || pre != 0) {
            int cur = pre;
            if (i >= 0) {
                cur += arr1[i];
            }
            if (j >= 0) {
                cur += arr2[j];
            }
            if (cur >= 2) {
                list.add(cur - 2);
                pre = -1;
            } else if (cur >= 0) {
                list.add(cur);
                pre = 0;
            } else {
                list.add(1);
                pre = 1;
            }
            i--;
            j--;
        }
        while (list.size() > 1 && list.get(list.size() - 1) == 0) {
            list.remove(list.size() - 1);
        }
        int[] ans = new int[list.size()];
        for (int k = 0; k < ans.length; k++) {
            ans[k] = list.get(list.size() - 1 - k);
        }
        return ans;
    }
}
