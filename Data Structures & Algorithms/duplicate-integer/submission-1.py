class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = len(list(set(nums)))
        return n!=nums
        