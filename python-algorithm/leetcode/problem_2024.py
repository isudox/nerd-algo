"""2024. Maximize the Confusion of an Exam
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_cnts = [0]
        f_cnts = [0]
        for key in answerKey:
            if key == 'T':
                t_cnts.append(t_cnts[-1] + 1)
                f_cnts.append(f_cnts[-1])
            else:
                f_cnts.append(f_cnts[-1] + 1)
                t_cnts.append(t_cnts[-1])
        i, j = 1, len(answerKey)  # sliding window size
        ans = 1
        while i <= j:
            mid = i + (j - i) // 2
            ok = False
            for x in range(mid, len(t_cnts)):
                if min(t_cnts[x] - t_cnts[x - mid], f_cnts[x] - f_cnts[x - mid]) <= k:
                    ok = True
                    break
            if ok:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1
        return ans

    def max_consecutive_answers(self, answerKey: str, k: int) -> int:
        def helper(ch: str) -> int:
            ret = 0
            left, cnt = 0, 0
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    cnt += 1
                while cnt > k:
                    if answerKey[left] != ch:
                        cnt -= 1
                    left += 1
                ret = max(ret, right- left + 1)
            return ret

        return max(helper('T'), helper('F'))
