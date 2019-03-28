package com.leetcode.solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 39. Combination Sum
 * https://leetcode.com/problems/combination-sum/
 *
 * Given a set of candidate numbers (candidates) (without duplicates)
 * and a target number (target), find all unique combinations in candidates
 * where the candidate numbers sums to target.
 *
 * The same repeated number may be chosen from candidates unlimited number of
 * times.
 *
 * Note:
 *
 *   All numbers (including target) will be positive integers.
 *   The solution set must not contain duplicate combinations.
 *
 * Example 1:
 *
 *   Input: candidates = [2,3,6,7], target = 7,
 *   A solution set is:
 *   [
 *     [7],
 *     [2,2,3]
 *   ]
 *
 * Example 2:
 *
 *   Input: candidates = [2,3,5], target = 8,
 *   A solution set is:
 *   [
 *     [2,2,2,2],
 *     [2,3,3],
 *     [3,5]
 *   ]
 */
public class CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), ans);

        return ans;
    }

    private void backtrack(int[] candidates, int target, int start, List<Integer> list, List<List<Integer>> ans) {
        for (int i = start; i < candidates.length; i++) {
            int num = candidates[i];
            if (target < num) {
                break;
            }
            list.add(num);
            if (target == num) {
                ans.add(new ArrayList<>(list));
                list.remove(list.size() - 1);
                break;
            }
            backtrack(candidates, target - num, i, list, ans);
            list.remove(list.size() - 1);
        }
    }
}
