class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recursion(stack, s, count):
            if count == n and len(stack) == 0:
                ans.append(s)
                return
            if count != n:
                stack.append(0)
                recursion(stack, s + '(', count + 1)
                stack.pop()
            if len(stack) != 0:
                stack.pop()
                recursion(stack, s + ')', count)
                stack.append(0)
        recursion([], '', 0)
        return sorted(ans)