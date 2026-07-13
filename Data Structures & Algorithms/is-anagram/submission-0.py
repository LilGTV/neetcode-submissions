class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChars = {}
        for c in s:
            if c in sChars:
                sChars[c] += 1
            else:
                sChars[c] = 1
        tChars = {}
        for c in t:
            if c in tChars:
                tChars[c] += 1
            else:
                tChars[c] = 1

        for c in sChars:
            if c not in tChars:
                return False
            if tChars[c] != sChars[c]:
                return False
        return True