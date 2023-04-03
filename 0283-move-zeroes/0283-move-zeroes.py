class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        delete = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                delete.append(i)
        for i in delete:
            nums.pop(i)
            nums.append(0)