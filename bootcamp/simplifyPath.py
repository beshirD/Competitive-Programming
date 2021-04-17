class Solution:
    def simplifyPath(self, path: str) -> str:
        direc = path.split("/")
        stack = []
        for di in direc:
            if stack and di == "..":
                stack.pop()
            elif di and di != "." and di != "..":
                stack.append(di)
        return "/" + "/".join(stack)
        