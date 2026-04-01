class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myhash = {}
        temp = []
        temp1 = []


        for i in range(len(nums)):
            if nums[i] not in myhash:
                myhash[nums[i]] = 1
            else:
                myhash[nums[i]] += 1
        
        for num in myhash:
            temp.append((myhash[num], num))
        temp.sort(reverse=True)

        for i in range(k):
            temp1.append(temp[i][1])
        return temp1