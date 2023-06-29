package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1253. Reconstruct a 2-Row Binary Matrix
 * https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
 */
public class Problem1253 {
    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> upperRow = new ArrayList<>(), lowerRow = new ArrayList<>();
        for (int i = 0; i < colsum.length; i++) {
            upperRow.add(0);
            lowerRow.add(0);
        }
        ans.add(upperRow);
        ans.add(lowerRow);
        List<Integer> oneIndex = new ArrayList<>();
        for (int i = 0; i < colsum.length; i++) {
            if (colsum[i] == 1) {
                oneIndex.add(i);
            } else if (colsum[i] == 2) {
                upperRow.set(i, 1);
                lowerRow.set(i, 1);
                if (--upper < 0 || --lower < 0) {
                    return new ArrayList<>();
                }
            }
        }
        if (oneIndex.size() != upper + lower) {
            return new ArrayList<>();
        }
        for (int i = 0; i < oneIndex.size(); i++) {
            int idx = oneIndex.get(i);
            if (i < upper) {
                upperRow.set(idx, 1);
            } else {
                lowerRow.set(idx, 1);
            }
        }
        return ans;
    }
}
