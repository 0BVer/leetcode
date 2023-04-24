class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == target:
                    return i
            
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            
        return -1