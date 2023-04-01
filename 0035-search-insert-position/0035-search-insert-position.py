class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ran = 0, len(nums) - 1
        while ran[1] >= ran[0]:
            mid = (ran[1] - ran[0]) // 2 + ran[0]
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                ran = mid + 1, ran[1]
            else:
                ran = ran[0], mid - 1
        return ran[0]