class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = {}

        for i, n in enumerate(nums):
            needed = target - n
            if needed in myhash:
                return [myhash[needed], i]
            myhash[n] = i