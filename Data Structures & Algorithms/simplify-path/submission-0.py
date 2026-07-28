class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = [] 

        for elem in paths:
            if elem == "..":
                if stack: 
                    stack.pop() 
            elif elem != "" and elem != '.':
                stack.append(elem)

        return '/' + '/'.join(stack)