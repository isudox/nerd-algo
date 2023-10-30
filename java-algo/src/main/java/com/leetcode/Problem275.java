package com.leetcode;

/**
 * 275. H-Index II
 * https://leetcode.com/problems/h-index-ii
 */
public class Problem275 {
    public int hIndex(int[] citations) {
        int ans = 0;
        int n = citations.length;
        int lo = citations[0], hi = citations[n - 1], mid;
        while (lo <= hi) {
            mid = (lo + hi) >> 1;
            int cnt = n - binarySearch(citations, mid);
            if (cnt >= mid) {
                ans = Math.max(ans, mid);
                lo = mid + 1;
            } else {
                ans = Math.max(ans, cnt);
                hi = mid - 1;
            }
        }
        return ans;
    }

    private int binarySearch(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1, mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (nums[mid] >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
