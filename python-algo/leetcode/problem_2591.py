class Solution:
    def distMoney(self, money: int, children: int) -> int:
        def helper(m: int, c: int) -> bool:
            if m < c or (m != 0 and c == 0) or (m == 4 and c == 1):
                return False
            return True

        if money < children:
            return -1
        if children == 1 and money == 4:
            return -1
        ans = min(money // 8, children)
        while ans >= 0:
            if helper(money - ans * 8, children - ans):
                return ans
            ans -= 1
        return -1
