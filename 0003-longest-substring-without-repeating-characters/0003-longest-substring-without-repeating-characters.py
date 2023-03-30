class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_l = 0

        if len(s) == 0: return 0
        
        char = set()
        for i in range(len(s)):
            char = set(s[i])
            if i == len(s) - 1: break

            for j in range(i + 1, len(s)):
                if s[j] in char: break
                else: char.add(s[j])

            if len(char) > max_l: max_l = len(char)
            char = set()

        if len(char) > max_l: return len(char)
        return max_l