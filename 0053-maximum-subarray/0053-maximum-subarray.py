class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        temp=0
        for i in range(len(nums)):
            if temp<0: # 누적된 최대값이 음수일 경우 버림, 즉 더한 값이 양수일때만 가져감
                temp=0
            temp+=nums[i]
            if temp>max_sum: 
                max_sum=temp
        return max_sum