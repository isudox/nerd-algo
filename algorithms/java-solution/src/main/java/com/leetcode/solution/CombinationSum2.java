package com.leetcode.solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 40. Combination Sum II
 * https://leetcode.com/problems/combination-sum-ii/
 *
 * Given a collection of candidate numbers (candidates) and
 * a target number (target), find all unique combinations in candidates where
 * the candidate numbers sums to target.
 *
 * Each number in candidates may only be used once in the combination.
 *
 * Note:
 *
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 * Example 1:
 *
 * Input: candidates = [10,1,2,7,6,1,5], target = 8,
 * A solution set is:
 * [
 *   [1, 7],
 *   [1, 2, 5],
 *   [2, 6],
 *   [1, 1, 6]
 * ]
 * Example 2:
 *
 * Input: candidates = [2,5,2,1,2], target = 5,
 * A solution set is:
 * [
 *   [1,2,2],
 *   [5]
 * ]
 */
public class CombinationSum2 {

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
