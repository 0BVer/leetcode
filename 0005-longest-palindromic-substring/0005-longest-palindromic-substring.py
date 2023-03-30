class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        max_len = 0
        max_s = ''

        for i in range(len(s)):
            for j in range(len(s)):
                if s[j] == s[i]:
                    temp = s[i : j + 1]
                    if temp == temp[::-1] and len(temp) > max_len:
                        max_len = len(temp)
                        max_s = temp

        return max_s