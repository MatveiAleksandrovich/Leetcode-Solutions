# 22. Generate Parentheses
# Topics: Stack, Recursion, Backtracking


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backracking(left_brackets: int, right_brackets: int):
            # Set the base case
            if left_brackets == right_brackets == n:
                result.append("".join(stack))
                return
            # if amount of openning brackets less than allowed
            if left_brackets < n:
                stack.append("(")
                backracking(left_brackets+1, right_brackets)
                stack.pop()
            # if amount of closing brackets 
            if right_brackets < left_brackets:
                stack.append(")")
                backracking(left_brackets, right_brackets+1)
                stack.pop()
            
        backracking(0, 0)
        return result
