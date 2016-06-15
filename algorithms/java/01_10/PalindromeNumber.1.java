// PalindromeNumber.java v1.1
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        if (x == 0) return true;
        int count = 0;
        int temp = x;
        while (temp > 0) {
            temp /= 10;
            count++;
        }
        for (int i = count; i > 0; i -= 2) {
            if (x / this.pow(10, i - 1) != x % 10) return false;
            x = (x % this.pow(10, i - 1)) / 10;
        }
        return true;
    }
    private int pow(int x, int y) {
        int z = 1;
        for (; y > 0; y--) z *= x;
        return z;
    }
}