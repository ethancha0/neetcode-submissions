class Solution:
    def simplifyPath(self, path: str) -> str:
        #treat / as delimiter 
        files = path.split('/')
        stack = [] 

        for f in files:
            if f == '' or f == '.':
                continue
            if f == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(f)


        #join back with /
        return '/' + "/".join(stack)
