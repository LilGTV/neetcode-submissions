class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for nr in nums:
            if nr in exists.keys():
                return True
            exists[nr] = 1
        return False