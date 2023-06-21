class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def combi(temp: List[int], left_value: List[int]):
            if sum(temp) == target:
                answer.append(temp)
                return
            elif sum(temp) > target:
                return

            for c in range(len(left_value)):
                combi(temp + [left_value[c]], left_value[c:])
            
        combi([], candidates)
        
        return answer