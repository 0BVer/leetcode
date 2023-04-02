class Solution:
    def climbStairs(self, n: int) -> int:
        mem = 1, 0 # 1로 끝나는 것, 2로 끝나는 것
        for _ in range(n):
            mem = mem[0] + mem[1], mem[0]
        return mem[0]
                    
                    