public class Solution {
    public int myAtoi(String str) {
        if (str == null || Objects.equals(str, ""))
            return 0;
        if (str.charAt(0) == '-')
            return subAtoi(str.substring(1), true);
        if (str.charAt(0) == '+')
            return subAtoi(str.substring(1), false);
        if (str.charAt(0) == ' ')
            return myAtoi(str.substring(1));
        return subAtoi(str, false);
    }

    private int subAtoi(String str, boolean neg) {
        if (str == null || str.equals("")) {
            System.out.println("a");
            return 0;
        }
        int res = 0;
        for (int i = 0; i < str.length(); i++) {
            if (!Character.isDigit(str.charAt(i)))
                return res;
            int digit = Character.getNumericValue(str.charAt(i));
            if (neg) {
                if (i == 9) {
                    int diff = res - Integer.MIN_VALUE / 10;
                    if (diff < 0 || (diff == 0 && digit > 8))
                        return Integer.MIN_VALUE;
                }
                if (i >= 10)
                    return Integer.MIN_VALUE;
                res = 10 * res - digit;
            } else {
                if (i == 9) {
                    int diff = res - Integer.MAX_VALUE / 10;
                    if (diff > 0 || (diff == 0 && digit > 7))
                        return Integer.MAX_VALUE;
                }
                if (i >= 10)
                    return Integer.MAX_VALUE;
                res = digit + 10 * res;
            }
        }
        return res;
    }
}