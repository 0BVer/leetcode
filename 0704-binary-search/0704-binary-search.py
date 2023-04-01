class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ran = 0, len(nums) - 1
        while ran[1] >= ran[0]:
            mid = ran[1] - ran[0] // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                 ran = ran[0], mid - 1
            elif target > nums[mid]:
                ran = mid + 1, ran[1]
            
        return -1