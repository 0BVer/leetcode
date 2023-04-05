class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split(' ')
        return ' '.join(t[::-1] for t in text)