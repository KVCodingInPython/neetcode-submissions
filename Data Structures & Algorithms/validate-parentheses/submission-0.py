class Solution:
    def isValid(self, s: str) -> bool:
        # Odd-length strings can't be valid
        if len(s) % 2 != 0:
            return False
        
        stack = []
        # Map closing brackets to their expected opening bracket
        matching_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_map:
                # If it's a closing bracket:
                # Check if stack is empty or if top doesn't     match             expected opening bracket
                if not stack or stack[-1] != matching_map[char]:
                    return False
                stack.pop()  # Matched successfully, remove opening bracket
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)

        # Valid if all opening brackets were popped and matched
        return len(stack) == 0
            

        