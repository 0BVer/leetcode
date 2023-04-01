# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ran = 1, n
        if isBadVersion(1): return 1
        while ran[1] - ran[0] > 1:
            mid = (ran[1] - ran[0]) // 2 + ran[0]
            if not isBadVersion(mid):
                ran = mid, ran[1]
            else:
                ran = ran[0], mid

        return ran[1]