class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen and seen[complement] != i:
                return [seen[complement], i]
            seen[nums[i]] = i