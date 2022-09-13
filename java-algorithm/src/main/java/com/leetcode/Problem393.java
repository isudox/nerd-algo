package com.leetcode;

/**
 * 393. UTF-8 Validation
 * https://leetcode.com/problems/utf-8-validation/
 */
class Problem393 {
    public boolean validUtf8(int[] data) {
        String[] nums = new String[data.length];
        for (int i = 0; i < data.length; i++) {
            String bin = Integer.toBinaryString(data[i]);
            StringBuilder code = new StringBuilder();
            for (int j = 0; j < 8 - bin.length(); j++) {
                code.append("0");
            }
            code.append(bin);
            nums[i] = code.toString();
        }
        return check(nums, 0);
    }

    private boolean check(String[] nums, int pos) {
        if (pos == nums.length)
            return true;
        if (nums[pos].startsWith("10"))
            return false;
        int n = 1;
        if (nums[pos].charAt(0) == '1') {
            for (int i = 1; i < 8; i++) {
                if (nums[pos].charAt(i) == '0')
                    break;
                if (++n > 4)
                    return false;
            }
        }
        if (nums.length - pos < n)
            return false;
        for (int i = 1; i < n; i++) {
            if (!nums[pos + i].startsWith("10"))
                return false;
        }
        return check(nums, pos + n);
    }
}
