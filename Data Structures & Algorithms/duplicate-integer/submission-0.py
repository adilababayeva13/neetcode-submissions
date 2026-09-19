class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = len(list(set(nums)))
        n = len(nums)
        return n!=nums_set
        