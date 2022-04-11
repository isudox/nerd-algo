package com.misc;

import java.util.ArrayList;
import java.util.List;

/**
 * Amazon OA | Sum of Server Powers
 * https://leetcode.com/discuss/interview-question/1759431/amazon-oa-sum-of-server-powers
 *
 * min(1) * sum(1) = 1 * 1 =            1
 * min(1,3) * sum(1,3) = 1 * 4 =        4
 * min(1,3,4) * sum(1,3,4) = 1 * 8 =    8
 * min(3) * sum(3) = 3 * 3 =            9
 * min(3,4) * sum(3,4) = 3 * 7 =        21
 * min(4) * sum(4) =4 * 4 =             16
 * 1+4+8+9+21+16 =                      59
 */
public class SumOfPower {
    public int getSum(int[] nums) {
        int[] preSum = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            MonoStack ms = new MonoStack();
            for (int j = i; j < nums.length; j++) {
                ms.add(nums[j]);
                int sum = preSum[j + 1] - preSum[i];
                int min = ms.peek();
                ans += sum * min;
            }
        }
        return ans;
    }

    private static class MonoStack {
        private List<Integer> list;

        public MonoStack() {
            list = new ArrayList<>();
        }

        public void add(int num) {
            List<Integer> tmp = new ArrayList<>();
            while (!list.isEmpty() && list.get(list.size() - 1) < num) {
                tmp.add(list.remove(list.size() - 1));
            }
            list.add(num);
            while (!tmp.isEmpty()) {
                list.add(tmp.remove(tmp.size() - 1));
            }
        }

        public void remove(int num) {
            int lo = 0, hi = list.size() - 1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (list.get(mid) == num) {
                    list.remove(mid);
                    return;
                }
                if (list.get(mid) < num) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            }
            list.remove(lo);
        }

        public int peek() {
            return list.get(list.size() - 1);
        }
    }

    public static void main(String[] args) {
        SumOfPower p = new SumOfPower();
        System.out.println(p.getSum(new int[]{1, 3, 4}));
    }
}
