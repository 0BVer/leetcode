class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = nums[0]
        
        for i in range(1, len(nums)):
            if last < i:
                return False
            last = max(last, nums[i] + i)
        return last >= len(nums) - 1