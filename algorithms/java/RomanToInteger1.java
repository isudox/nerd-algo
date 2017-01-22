public class Solution {
    public int romanToInt(String s) {
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] ints = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        int res = 0;
        for (int i = 0; i < romans.length;) {
            int index = s.indexOf(romans[i]);
            if (index == 0) {
                res += ints[i];
                s = s.substring(index + romans[i].length());
            } else {
                i++;
            }
        }
        return res;
    }
}