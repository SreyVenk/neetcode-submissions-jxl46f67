class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        arr = []
        arr1 = []
        
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 1
            else:
                temp[nums[i]] += 1
        
        for num in temp:
            arr.append((temp[num], num))
        arr.sort(reverse=True)

        for j in range(k):
            arr1.append(arr[j][1])
        return arr1