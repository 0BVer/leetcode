class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        def dp(lst):
            memo = [0] * len(lst)
            memo[0] = lst[0]
            memo[1] = max(lst[:2])
        
            for i in range(2, len(lst)):
                memo[i] = max(memo[i - 2] + lst[i], memo[i - 1])
            
            return memo[-1]
        
        return max(dp(nums[:-1]), dp(nums[1:]))