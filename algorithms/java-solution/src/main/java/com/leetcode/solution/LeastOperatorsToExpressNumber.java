package com.leetcode.solution;

import java.util.HashMap;
import java.util.Map;

/**
 * 964. Least Operators to Express Number
 * https://leetcode.com/problems/least-operators-to-express-number/
 *
 * Given a single positive integer x, we will write an expression of the form
 * x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc.
 * is either addition, subtraction, multiplication, or division (+, -, *, or /).
 * For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
 *
 * When writing such an expression, we adhere to the following conventions:
 *
 *   The division operator (/) returns rational numbers.
 *   There are no parentheses placed anywhere.
 *   We use the usual order of operations: multiplication and division happens
 *   before addition and subtraction.
 *   It's not allowed to use the unary negation operator (-).  For example,
 *   "x - x" is a valid expression as it only uses subtraction, but "-x + x" is
 *   not because it uses negation.
 *
 * We would like to write an expression with the least number of operators such
 * that the expression equals the given target.  Return the least number of
 * operators used.
 *
 * Example 1:
 *
 * Input: x = 3, target = 19
 * Output: 5
 * Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
 *
 * Example 2:
 *
 * Input: x = 5, target = 501
 * Output: 8
 * Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.
 *
 * Example 3:
 *
 * Input: x = 100, target = 100000000
 * Output: 3
 * Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.
 *
 * Note:
 *
 * 2 <= x <= 100
 * 1 <= target <= 2 * 10^8
 */
public class LeastOperatorsToExpressNumber {

    private Map<String, Integer> memo = new HashMap<>();
    private int x;

    public int leastOpsExpressTarget(int x, int target) {
        this.x = x;
        return dp(0, target) - 1;
    }

    private int dp(int i, int target) {
        String code = "" + i + "#" + target;
        if (memo.containsKey(code)) {
            return memo.get(code);
        }
        int ans;
        if (target == 0) {
            ans = 0;
        } else if (target == 1) {
            ans = cost(i);
        } else if (i >= 39) {
            ans = target + 1;
        } else {
            int t = target / x;
            int r = target % x;
            ans = Math.min(r * cost(i) + dp(i + 1, t),
                    (x - r) * cost(i) + dp(i + 1, t + 1));
        }
        memo.put(code, ans);
        return ans;
    }

    private int cost(int x) {
        return x > 0 ? x : 2;
    }
}
