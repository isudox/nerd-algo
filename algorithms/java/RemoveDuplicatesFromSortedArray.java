public class Solution {
    public int removeDuplicates(int[] nums) {
        int count = nums.length;
        if (count < 2)
            return count;
        int left = 0, right = 1;
        while (right < count) {
            if (nums[left] == nums[right]) {
                right++;
            } else {
                nums[++left] = nums[right++];
            }
        }
        return left + 1;
    }
}