class Solution:
    def simplifyPath(self, path: str) -> str:
        absolute_path = path.split("/")
        canonical_path = []

        for dir in absolute_path:
            if not dir or dir == ".":
                continue
            elif dir == "..":
                if canonical_path:
                    canonical_path.pop()
            else:
                canonical_path.append(dir)

        return "/" + "/".join(canonical_path)