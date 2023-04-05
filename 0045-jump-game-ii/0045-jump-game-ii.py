class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 3: return l - 1
        s, e = 0, nums[0]
        count = 1
        
        while True:
            big = 0
            if e >= l - 1: return count
            count += 1
            s, e = e, max(nums[i] + i for i in range(s + 1, e + 1))
