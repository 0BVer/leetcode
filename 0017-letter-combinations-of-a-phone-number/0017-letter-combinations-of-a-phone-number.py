class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []
        nums = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        memo = [n for n in nums[int(digits[0])]]

        for d in range(1, len(digits)):
            temp = []
            for i in nums[int(digits[d])]:
                for m in memo:
                    temp.append(m + i)
            
            memo = temp

        return memo