class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p = nums[0], nums[0]
        last_max = max_p
        
        for i in range(1, len(nums)):
            max_p, min_p = max(max_p * nums[i], min_p * nums[i], nums[i]), min(max_p * nums[i], min_p * nums[i], nums[i])

            if max_p > last_max: last_max = max_p

        return max(last_max, max_p)