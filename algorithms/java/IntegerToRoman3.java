public class Solution {
    public String intToRoman(int num) {
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] ints = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < ints.length; i++) {
            while (num >= ints[i]) {
                res.append(romans[i]);
                num -= ints[i];
            }
        }
        return res.toString();
    }
}