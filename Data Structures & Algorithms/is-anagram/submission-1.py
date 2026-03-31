class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myhash = {}

        for i in range(len(s)):
            if s[i] not in myhash:
                myhash[s[i]] = 1
            else:
                myhash[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in myhash:
                return False
            else:
                myhash[t[j]] -= 1
            
            if myhash[t[j]] < 0:
                return False
        return True