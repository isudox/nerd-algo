public class Solution {
    public String intToRoman(int num) {
        String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] thousands = {"", "M", "MM", "MMM"};
        String[][] romans = {ones, tens, hundreds, thousands};
        String res = "";
        int len = String.valueOf(num).length();
        for (int i = len - 1; i >= 0; i--) {
            int x = num / pow(10, i);
            res = res + romans[i][x];
            num = num % pow(10, i);
        }
        return res;
    }

    private int pow(int x, int y) {
        int z = 1;
        for (; y > 0; y--) z *= x;
        return z;
    }
}