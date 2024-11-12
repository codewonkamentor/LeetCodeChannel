class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []
        for i, path in enumerate(path_list):
            if path == "..":
                if stack: stack.pop()
            elif path == "" or path == ".":
                continue
            else:
                stack.append(path)
        return "/" + "/".join(stack)
