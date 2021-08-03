package com.leetcode;

import java.util.*;

/**
 * 47. Permutations II
 * https://leetcode.com/problems/permutations-ii/
 *
 * Given a collection of numbers that might contain duplicates,
 * return all possible unique permutations.
 *
 * Example:
 *
 * Input: [1,1,2]
 * Output:
 * [
 *   [1,1,2],
 *   [1,2,1],
 *   [2,1,1]
 * ]
 */
public class Problem47 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        do {
            List<Integer> list = new ArrayList<>(nums.length);
            for (int num : nums)
                list.add(num);
            ans.add(list);
        } while (next(nums));
        return ans;
    }

    private boolean next(int[] nums) {
        if (nums.length < 2)
            return false;
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1])
            i--;
        if (i < 0)
            return false;
        int j = nums.length - 1;
        while (j > 0 && nums[j] <= nums[i])
            j--;
        swap(nums, i, j);
        int x = i + 1, y = nums.length - 1;
        while (x < y)
            swap(nums, x++, y--);
        return true;
    }

    private void swap(int[] nums, int x, int y) {
        nums[x] = nums[x] ^ nums[y];
        nums[y] = nums[x] ^ nums[y];
        nums[x] = nums[x] ^ nums[y];
    }

    public List<List<Integer>> permuteUnique2(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), new boolean[nums.length], ans);
        return ans;
    }

    private void backtrack(int[] nums, int pos, List<Integer> perm, boolean[] visited, List<List<Integer>> ans) {
        if (nums.length == pos)
            ans.add(new ArrayList<>(perm));
        Set<Integer> duplicates = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (visited[i] || duplicates.contains(nums[i]))
                continue;
            perm.add(nums[i]);
            duplicates.add(nums[i]);
            visited[i] = true;
            backtrack(nums, pos + 1, perm, visited, ans);
            perm.remove(perm.size() - 1);
            visited[i] = false;
        }
    }

}
