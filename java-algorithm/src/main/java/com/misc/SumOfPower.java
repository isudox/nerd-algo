package com.misc;

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
            int min = nums[i];
            for (int j = i; j < nums.length; j++) {
                if (nums[j] < nums[i]) {
                    min = nums[j];
                }
                int sum = preSum[j + 1] - preSum[i];
                ans += sum * min;
            }
        }
        return ans;
    }
}
