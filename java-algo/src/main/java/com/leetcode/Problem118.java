package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 118. Pascal's Triangle
 * https://leetcode.com/problems/pascals-triangle/
 */
public class Problem118 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        if (numRows == 0) return ans;
        for (int i = 1; i <= numRows; i++) {
            List<Integer> cur = new ArrayList<>();
            if (i == 1) {
                cur.add(1);
                ans.add(cur);
                continue;
            }
            if (i == 2) {
                cur.add(1);
                cur.add(1);
                ans.add(cur);
                continue;
            }
            List<Integer> pre = ans.get(ans.size() - 1);
            cur.add(1);
            for (int j = 0; j + 1 < ans.size(); j++) {
                cur.add(pre.get(j) + pre.get(j + 1));
            }
            cur.add(1);
            ans.add(cur);
        }
        return ans;
    }
}
