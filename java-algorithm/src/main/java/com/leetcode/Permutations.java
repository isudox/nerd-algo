package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 46. Permutations
 * https://leetcode.com/problems/permutations/
 *
 * Given a collection of *distinct* integers, return all possible permutations.
 *
 * Example:
 *
 * Input: [1,2,3]
 * Output:
 * [
 *   [1,2,3],
 *   [1,3,2],
 *   [2,1,3],
 *   [2,3,1],
 *   [3,1,2],
 *   [3,2,1]
 * ]
 */
public class Permutations {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> permutations = new ArrayList<>();
        int len = nums.length;
        if (len == 0) {
            permutations.add(new ArrayList<>());
            return permutations;
        }
        List<List<Integer>> prePermutations = permute(Arrays.copyOfRange(nums, 0, len - 1));
        for (List<Integer> permutation : prePermutations) {
            List<Integer> copy;
            for (int i = 0; i <= permutation.size(); i++) {
                copy = new ArrayList<>(permutation);
                copy.add(i, nums[len - 1]);
                permutations.add(copy);
            }
        }
        return permutations;
    }
}
