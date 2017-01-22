public class Solution {
    public static int reverse(int x) {
        boolean isNeg = false;
        long result = 0L;
        if (x == -2147483648) {
            return 0;
        }
        if (x < 0) {
            isNeg = true;
            x = -x;
        }
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        if (result > Integer.MAX_VALUE) {
            return 0;
        }
        if (isNeg) {
            result = -result;
        }

        return Math.toIntExact(result);
    }
}