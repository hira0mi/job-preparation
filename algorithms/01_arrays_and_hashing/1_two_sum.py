class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i, num in enumerate(nums):
            y = target-num
            if y in s:
                return [s[y], i]
            else:
                s[num] = i

        