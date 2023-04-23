class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]
        start, end = 0, len(nums) - 1
        while end >= start:
            if nums[start] == nums[end] == target:
                return [start, end]
            if nums[start] < target:
                start += 1
            if nums[end] > target:
                end -= 1

        return [-1, -1]