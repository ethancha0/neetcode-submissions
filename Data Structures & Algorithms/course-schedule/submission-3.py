class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap=[[] for _ in range(numCourses)]
        for pre, crs in prerequisites: 
            crsMap[crs].append(pre)

        visitedSet = set() 
        def dfs(course):
            if course in visitedSet: 
                return False 
            if course == []:
                return True 
            
            visitedSet.add(course) 
            for prereq in crsMap[course]:
                if not dfs(prereq):
                    return False

            visitedSet.remove(course)
            crsMap[course] = []

            return True 

        
        # call on every course in case disjoint 
        for pre, crs in prerequisites: 
            if not dfs(crs):
                return False 

        return True