public class Solution {
    public String intToRoman(int num) {
        String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] thousands = {"", "M", "MM", "MMM"};
        String[][] romans = {ones, tens, hundreds, thousands};
        String res = "";
        int digit = 0;
        while (num > 0) {
            int x = num % 10;
            res = romans[digit][x] + res;
            num = num / 10;
            digit++;
        }
        return res;
    }
}