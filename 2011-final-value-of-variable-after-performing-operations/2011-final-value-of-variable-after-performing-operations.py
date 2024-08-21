class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = {'++X':1, 'X++':1, '--X':-1, 'X--':-1}
        ans = 0
        for item in operations:
            ans += value[item]
        return ans
        