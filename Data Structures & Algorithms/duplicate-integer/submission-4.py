class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        someset = set()
        for i in nums:
            if i not in someset:
                someset.add(i)
            else:
                return True
        return False