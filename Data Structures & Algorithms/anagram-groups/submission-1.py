class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        somehash = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in somehash:
                somehash[key] = []
            somehash[key] += [word]
        return list(somehash.values())