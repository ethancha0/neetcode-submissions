class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course : prereqs 
        courses = [[] for i in range(numCourses)]
        for prereq, course in prerequisites: 
            courses[course].append(prereq)

        visitSet = set() 
        def dfs(course): 
            if course in visitSet: 
                return False 
            if len(courses[course]) == 0:  #course has no prereq 
                return True 

            visitSet.add(course)
            #call dfs on all its prereqs
            for prereq in courses[course]: 
                if not dfs(prereq):
                    return False #if one of them has cycle (false), return false 
            
            visitSet.remove(course)
            courses[course] = [] # Mark as verified to avoid redundant work

            return True 

        
        #call on every cell since some may be disconencted 
        for e in range(numCourses): 
            if not dfs(e):
                return False

        return True 

