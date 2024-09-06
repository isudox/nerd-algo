package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 40. Combination Sum II
 * https://leetcode.com/problems/combination-sum-ii/
 */
public class Problem40 {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), ans, 0);
        return ans;
    }

    private void backtrack(int[] candidates,
                           int target,
                           int start,
                           List<Integer> list,
                           List<List<Integer>> ans,
                           int lastPop) {
        for (int i = start; i < candidates.length; i++) {
            int num = candidates[i];
            if (num == lastPop) {
                continue;
            }
            if (target < num) {
                break;
            }
            list.add(num);
            if (target == num) {
                ans.add(new ArrayList<>(list));
                list.remove(list.size() - 1);
                break;
            }
            backtrack(candidates, target - num, i + 1, list, ans, lastPop);
            lastPop = list.remove(list.size() - 1);
        }
    }
}
