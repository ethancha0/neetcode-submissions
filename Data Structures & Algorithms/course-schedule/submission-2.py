class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for _ in range(numCourses)]

        for pre, crs, in prerequisites: 
            preMap[crs].append(pre)

        visitedSet = set() 

        def dfs(course):
            if course in visitedSet: 
                return False 
            if preMap[course] == []:
                return True 
        
            visitedSet.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False 
            
            visitedSet.remove(course)

            preMap[course] = [] # mark as safe

            return True 

        
        for i in range(numCourses-1):
            if not dfs(i):
                return False

        return True



