package com.contest;

import java.util.*;

public class Contest291 {
    public String removeDigit(String number, char digit) {
        char[] arr = number.toCharArray();
        String ans = "0";
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == digit) {
                String tmp = number.substring(0, i) + number.substring(i + 1);
                if (tmp.compareTo(ans) > 0) {
                    ans = tmp;
                }
            }
        }
        return ans;
    }

    public int minimumCardPickup(int[] cards) {
        Map<Integer, List<Integer>> store = new HashMap<>();
        for (int i = 0; i < cards.length; i++) {
            List<Integer> positions = store.getOrDefault(cards[i], new ArrayList<>());
            positions.add(i);
            store.put(cards[i], positions);
        }
        int ans = cards.length + 1;
        for (List<Integer> positions : store.values()) {
            if (positions.size() < 2) {
                continue;
            }
            int tmp;
            for (int i = 1; i < positions.size(); i++) {
                tmp = positions.get(i) - positions.get(i - 1) + 1;
                if (tmp < ans) {
                    ans = tmp;
                }
            }
        }
        return ans == cards.length + 1 ? -1 : ans;
    }

    public int countDistinct(int[] nums, int k, int p) {
        int n = nums.length;
        int[] valid = new int[n];
        for (int i = 0; i < n; i++) {
            if (nums[i] % p == 0) {
                valid[i] = 1;
            }
        }
        int[] preCounts = new int[n + 1];
        for (int i = 0; i < n; i++) {
            preCounts[i + 1] = preCounts[i] + valid[i];
        }
        int ans = 0;
        Set<String> seen = new HashSet<>();
        for (int i = 0; i < preCounts.length; i++) {
            for (int j = i + 1; j < preCounts.length; j++) {
                if (preCounts[j] - preCounts[i] <= k) {
                    String key = encode(nums, i, j);
                    if (!seen.contains(key)) {
                        seen.add(key);
                        ans++;
                    }
                }
            }
        }
        return ans;
    }

    private String encode(int[] nums, int start, int end) {
        StringBuilder sb = new StringBuilder();
        for (int i = start; i < end; i++) {
            sb.append("-").append(nums[i]);
        }
        return sb.toString();
    }
}
