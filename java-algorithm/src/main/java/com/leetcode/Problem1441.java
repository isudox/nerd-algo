package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1441. Build an Array With Stack Operations
 * https://leetcode.com/problems/build-an-array-with-stack-operations/
 */
public class Problem1441 {
    public List<String> buildArray(int[] target, int n) {
        List<String> ans = new ArrayList<>();
        int cur = 1;
        for (int num : target) {
            while (cur != num) {
                ans.add("Push");
                ans.add("Pop");
                cur++;
            }
            ans.add("Push");
            cur++;
        }
        return ans;
    }
}
