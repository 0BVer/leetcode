class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1
        while e > s:
            ns = numbers[s] + numbers[e]
            if ns == target:
                return [s + 1, e + 1]
            elif ns < target:
                s += 1
            else:
                e -= 1