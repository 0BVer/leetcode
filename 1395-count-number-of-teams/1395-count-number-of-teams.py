class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        length = len(rating)

        for pivot in range(1, length - 1):
            left = len([l for l in rating[:pivot] if l < rating[pivot]])
            right = len([r for r in rating[pivot + 1:] if rating[pivot] < r])
            count += left * right
            count += (pivot - left) * (length - pivot - right - 1)
        
        return count