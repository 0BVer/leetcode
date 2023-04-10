class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        memo = [[0, 0] for _ in nums]
        last = 0

        if nums[0] > 0:     memo[0][0] = 1
        elif nums[0] < 0:   memo[0][1] = 1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                if memo[i - 1][1] == 0: # 최근 음수였던 적이 업서엇 누적 될 수가 없는 경우
                    memo[i][0] = memo[i - 1][0] + 1
                else:
                    memo[i] = [memo[i - 1][0] + 1, memo[i - 1][1] + 1]

            elif nums[i] < 0:
                if memo[i - 1][1] == 0: # 최근 음수였던 적이 없어서 누적 될 수가 없는 경우
                    memo[i][1] = memo[i - 1][0] + 1
                else:
                    memo[i] = [memo[i - 1][1] + 1, memo[i - 1][0] + 1]

            last = max(memo[i][0], last)

        return max(last, memo[-1][0])