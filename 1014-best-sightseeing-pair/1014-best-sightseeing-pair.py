class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len(values) == 2: return sum(values) - 1
        mi = max(values[0], values[1] + 1)
        memo = max(values[0] + values[1] - 1, mi + values[2] - 2)

        for i in range(3, len(values)):
            mi = max(mi, i - 1 + values[i - 1])
            memo = max(memo, mi + values[i] - i)
        return memo