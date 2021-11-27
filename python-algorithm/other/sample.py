from typing import List


def div(nums: List[int], base: int) -> List[float]:
    ret = []
    for num in nums:
        ret.append(num / base * 100)
    return ret


def div2(nums1: List[int], nums2: List[int]) -> List[float]:
    ret = []
    for i in range(len(nums1)):
        ret.append(nums1[i] / nums2[i] * 100)
    return ret


def avg(nums: List[int]) -> float:
    return sum(nums) / len(nums)


if __name__ == '__main__':
    nums = [1996836, 61, 56221,2556, 25283]
    nums2 = [1996731, 61, 56217, 2556, 25283]
    # base = 9819688
    # ans = div(nums, base)
    # print(ans)
    print(sum(nums))
    print(div2(nums2, nums))
    print(sum(nums2) / sum(nums) * 100)
