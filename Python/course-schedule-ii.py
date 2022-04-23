class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        lookup = {index: [] for index in range(numCourses)}
        
        for course, prereq in prerequisites:
            lookup[course].append(prereq)
            
        output = []
        
        visited, cycle = set(), set()
        
        def dfs(course):
            
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            
            for prereq in lookup[course]:
                if not dfs(prereq):
                    return False
                
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            
            return True
            
            
        for index in range(numCourses):
            if not dfs(index):
                return []
            
        return output
