class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build + fill course:prereq
        preMap = [[] for _ in range(numCourses)]
        for prereq, course in prerequisites: 
            preMap[course].append(prereq)


        visitSet = set() 
        def dfs(crs): 
            if crs in visitSet: 
                return False 
            if preMap == []:    #class has no prereq
                return True 

            visitSet.add(crs)

            #call dfs on all the crs prereq
            for pre in preMap[crs]: # IMPORTANT: CHECK WHAT THIS DOES
                if not dfs(pre):
                    return False 

            visitSet.remove(crs)

            return True

        #call on every course since some may be disconnected
        for i in range(numCourses):
            if not dfs(i):
                return False 
        return True 
            