"""
LeetCode - Valid Parentheses

Time complexity is O(n) because I used a stack with a dictionary lookup so only a single pass through the list

Space complexity is O(n) worst case with the worst case scenario being all opening brackets because every character would get pushed onto the stack

A brute force approach would be to scan the string for adjacent pairs and remove them until no more pairs are found or the string is empty. This method would cost O(n^2) time. Using the stack is an optimized approach since it only looks at each character once. It also uses the stack to keep track of unmatch openers so not rescanning is needed. 
"""
class Solution(object):
    def isValid(self, s):
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = [] 

        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]: 
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not stack 


if __name__ == "__main__":
	sol = Solution()

	assert sol.isValid("([)]") == false

	assert sol.isValid("()") == true

	assert sol.isValid("([])") == true

	print ("Passed")