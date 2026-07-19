class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites: 
            adjList[course].append(prereq) 

        visited = set() 

        def dfs(course):
            if course in visited: 
                return False
            if adjList[course] == []:
                return True 

            visited.add(course) 

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False 

            visited.remove(course) 
            adjList[course] = []
            return True

        
        #check every course 
        for pre, course in prerequisites: 
            if not dfs(course):
                return False

        return True

        




