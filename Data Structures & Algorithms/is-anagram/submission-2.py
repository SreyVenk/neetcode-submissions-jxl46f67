class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = {}

        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = 1
            else:
                temp[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in temp:
                return False
            else:
                temp[t[j]] -= 1
            if temp[t[j]] < 0:
                return False
        return True