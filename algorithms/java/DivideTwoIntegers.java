public class Solution {
    public int divide(int dividend, int divisor) {
        if (divisor == 0 || dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        int result = 0;
        boolean positive = dividend > 0 == divisor > 0;
        long dividend1 = dividend == Integer.MIN_VALUE ? 2147483648 : Math.abs(dividend);
        long divisor1 = divisor == Integer.MIN_VALUE ? 2147483648L : Math.abs(divisor);
        int i = 0;
        while (divisor1 << (i + 1) <= dividend1)
            i++;
        while (dividend1 >= divisor1) {
            if (dividend1 >= divisor1 << i) {
                result = result + (1 << i);
                dividend1 = dividend1 - (divisor1 << i);
            }
            i--;
        }
        return positive ? result : -result;
    }
}
