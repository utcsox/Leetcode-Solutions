class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = {index: [] for index in range(numCourses)}
        
        for course, prereq in prerequisites:
            mapping[course].append(prereq)
        
        visitSet = set()
        
        def dfs(course):
            
            if course in visitSet:
                return False
            
            if mapping[course] == []:
                return True
            
            visitSet.add(course)
            
            for pre in mapping[course]:
                if not dfs(pre):
                    return False
                
            visitSet.remove(course)
            mapping[course] = []
            
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
