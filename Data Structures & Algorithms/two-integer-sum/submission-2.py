class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = {}

        for index, value in enumerate(nums):
            result = target - value
            if result not in myhash:
                myhash[value] = index
            else:
                return [myhash[result], index]