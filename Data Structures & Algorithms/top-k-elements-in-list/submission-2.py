class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        temp = []
        sorted_temp = []


        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        
        for num in count:
            temp.append((count[num], num))

        temp.sort(reverse=True)

        for j in range(k):
            sorted_temp.append(temp[j][1])
        return sorted_temp