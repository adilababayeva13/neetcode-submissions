class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = len(set(nums))
        return n!=nums
        