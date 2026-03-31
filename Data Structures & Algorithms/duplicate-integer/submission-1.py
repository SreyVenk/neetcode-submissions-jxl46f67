class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash = {}

        for i in range(len(nums)):
            if nums[i] not in myhash:
                myhash[nums[i]] = 0
            else:
                return True
        return False