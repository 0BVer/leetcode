class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = nums[0] if nums[0] >= nums[1] else nums[1]
        
        for i in range(2, len(nums)):
            memo[i] = memo[i - 2] + nums[i] if memo[i - 2] + nums[i] >= memo[i - 1] else memo[i - 1]
        
        return memo[-1]