class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def rec(l, t):
            s, e = 0, len(l) - 1
            while e >= s:
                mid = (e - s) // 2 + s
                if l[mid] == t:
                    return mid
                elif l[mid] > t:
                    e = mid - 1
                else:
                    s = mid + 1
            return -1
        for i in range(len(numbers)):
            t = rec(numbers[i + 1:], target - numbers[i])
            if t != -1:
                return [i + 1, t + i + 2]