class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        
        for x in s:
            if x.isalnum():
                word += x.lower()
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        return True