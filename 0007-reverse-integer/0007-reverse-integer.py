class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:   
            t = int(str(x * -1)[::-1]) * -1
            if t < 2 ** 31 * -1:    return 0
            else:                   return t
        else:
            t = int(str(x)[::-1])
            if 2 ** 31 < t:         return 0
            return                  t