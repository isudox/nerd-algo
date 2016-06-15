// PalindromeNumber.java v1.2
public class Solution {
    public boolean isPalindrome(int x) {
if (x < 0) return false;
        int digits = 0;
        int temp = x;
        while (temp > 0) {
            temp /= 10;
            digits++;
        }
        int j = digits;
        for (int i = 1; j > i; i++, j--) {
            if (digit(x, digits, j) != digit(x, digits, i)) return false;
        }
        return true;
    }
    private int pow(int x, int y) {
        int z = 1;
        for (; y > 0; y--) z *= x;
        return z;
    }
    private int digit(int x, int i, int j) {
        return x / pow(10, j - 1) % 10;
    }
}