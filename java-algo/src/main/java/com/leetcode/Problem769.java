package com.leetcode;

/**
 * 769. Max Chunks To Make Sorted
 * https://leetcode.com/problems/max-chunks-to-make-sorted/
 */
class Problem769 {
    public int maxChunksToSorted(int[] arr) {
        int i = 0, j = 0, ans = 0, n = arr.length;
        int target = 0;
        int min = n, max = -1;
        boolean found = false;
        while (j < n) {
            min = Math.min(arr[j], min);
            max = Math.max(arr[j], max);
            if (arr[j] == target) {
                found = true;
            }
            if (found && max - min == j - i) {
                ans++;
                target = max + 1;
                min = n;
                max = -1;
                found = false;
            }
            j++;
        }
        return ans;
    }
}
