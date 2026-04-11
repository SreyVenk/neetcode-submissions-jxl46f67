class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "A" + s
        return result

    def decode(self, str):
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "A":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res