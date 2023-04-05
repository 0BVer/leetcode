class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [0] * len(nums)
        memo[0] = nums[0]
        
        for i in range(1, len(nums)):
            if memo[i - 1] < i:
                return False
            memo[i] = max(memo[i - 1], nums[i] + i)
        return memo[-1] >= len(nums) - 1