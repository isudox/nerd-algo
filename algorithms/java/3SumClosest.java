// ThreeSumClosest.java
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int sum = Integer.MAX_VALUE;
        int diff = Integer.MAX_VALUE;
        int count = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < count; i++) {
            int j = i + 1, k = count - 1;
            while (j < k) {
                int curSum = nums[i] + nums[j] + nums[k];
                int curDiff = curSum - target;
                if (curDiff == 0) return curSum;
                diff = Math.abs(diff) < Math.abs(curDiff) ? diff : curDiff;
                sum = target + diff;
                if (curDiff >= 0) {
                    k--;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                } else {
                    j++;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                }
            }
        }
        return sum;
    }
}
