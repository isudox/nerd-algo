"""2512. Reward Top K Students
https://leetcode.com/problems/reward-top-k-students
"""
import collections
from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str],
                    negative_feedback: List[str],
                    report: List[str],
                    student_id: List[int],
                    k: int) -> List[int]:
        scores = []
        groups = collections.defaultdict(list)
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        for i, sid in enumerate(student_id):
            rep = report[i]
            score = 0
            for word in rep.split(' '):
                if word in positive_feedback:
                    score += 3
                elif word in negative_feedback:
                    score -= 1
            if score not in groups:
                scores.append(score)
            groups[score].append(sid)
        ans = []
        scores.sort(reverse=True)
        for s in scores:
            groups[s].sort()
            j = min(k, len(groups[s]))
            ans += groups[s][:j]
            k -= j
            if k == 0:
                break
        return ans
