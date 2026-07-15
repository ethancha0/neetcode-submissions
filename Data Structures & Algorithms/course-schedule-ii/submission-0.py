class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        self.ans = []

        crsMap = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites: 
            crsMap[crs].append(pre)

        visitingSet = set() 
        visitedSet = set()

        def dfs(course):
            if course in visitedSet:  #already done
                return True 
            elif course in visitingSet: #cycle found
                return False 

            visitingSet.add(course)

            for prereq in crsMap[course]:
                if not dfs(prereq):
                    return False
            
            visitingSet.remove(course)
            visitedSet.add(course)
            self.ans.append(course)

            return True

        
        #call on every 
      #  for pre, crs in prerequisites:
       #     if not dfs(crs):
        #        return []

        for i in range(numCourses):
            if i not in visitedSet: 
                if not dfs(i): 
                    return []
        
        return self.ans
