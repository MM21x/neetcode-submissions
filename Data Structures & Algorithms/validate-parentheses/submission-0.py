class Solution:
    def isValid(self, s: str) -> bool:
        # our stack: stores opening brackets we haven't closed yet
        stack = []

        # closing bracket -> the opening bracket it belongs with
        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            # is this a closing bracket?
            if char in pairs:
                # if nothing is open, or the last opener is the wrong type, it's invalid
                if not stack or stack[-1] != pairs[char]:
                    return False

                # it matched, so remove that opener
                stack.pop()

            # otherwise it's an opening bracket
            else:
                # save it until we find its closer
                stack.append(char)

        # if the stack is empty, every bracket got closed
        # if not, some openers were never closed
        return not stack