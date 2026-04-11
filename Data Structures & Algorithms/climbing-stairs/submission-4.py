class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        arr = [1, 2]
        x = 0
        y = 1
        while y < n:
            arr.append(arr[x] + arr[y])
            x += 1
            y += 1
        return arr[n-1]