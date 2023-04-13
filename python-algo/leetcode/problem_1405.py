"""1405. Longest Happy String
https://leetcode.com/problems/longest-happy-string/
"""


def longest_diverse_string(a: int, b: int, c: int) -> str:
    ans = []
    cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
    while True:
        cnt.sort(key=lambda x: -x[0])
        has_next = False
        for i, (c, ch) in enumerate(cnt):
            if c <= 0:
                break
            if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                continue
            has_next = True
            ans.append(ch)
            cnt[i][0] -= 1
            break
        if not has_next:
            return ''.join(ans)
