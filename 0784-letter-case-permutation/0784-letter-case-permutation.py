class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        exist = set()
        index = [i for i in range(len(s)) if not s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]


        def per(s):
            if s in exist:
                return
            
            exist.add(s)

            for i in index:
                if s[i].islower():
                    new_s = s[:i] + s[i].upper() + s[i+1:]
                    per(new_s)
                    new_s = s[:i] + s[i].lower() + s[i+1:]
                else:
                    new_s = s[:i] + s[i].lower() + s[i+1:]
                    per(new_s)
                    new_s = s[:i] + s[i].upper() + s[i+1:]
            
        per(s)
        return list(exist)