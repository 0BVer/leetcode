class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_v = nums[0]
        max_v = nums[0]
        l = len(nums)

        # 내부 순환
        temp = 0
        temp += nums[0]
        for i in range(1, l):
            if temp < 0:
                temp = 0
            temp += nums[i]
            if temp > max_v: max_v = temp
        
        # 외부 순환
        temp = 0
        temp += nums[0]
        for i in range(1, l):
            if temp > 0:
                temp = 0
            temp += nums[i]
            if temp < min_v: min_v = temp

        if min_v >= 0 or sum(nums) - min_v == 0: return max_v # 만약 외부 순환이 성립하지 않는 경우
        return max(sum(nums) - min_v, max_v)