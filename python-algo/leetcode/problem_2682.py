from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        nums = [1 + i for i in range(n)]
        nums[0] = 0
        i, pos = 1, 0
        while True:
            pos = (pos + i * k) % n
            if nums[pos] == pos:  # 之前已经接过球
                break
            nums[pos] -= 1
            i += 1
        return [e for i, e in enumerate(nums) if e > i]
