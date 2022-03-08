"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Return true if you can finish all courses. Otherwise, return false.

Backtracking solution.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        course_dep = {i: [] for i in range(numCourses)}
        visited = set()
        
        for pre_req in prerequisites:
            crs = pre_req[0]
            dep = pre_req[1]

            course_dep[crs].append(dep)
        
        
        def dfs(crs):
            # already visited 
            if crs in visited:
                return False
            
            # doesn't have dep, so we can visit this
            if course_dep[crs] == []:
                return True
            
            visited.add(crs)
            
            # since we know this has deps, run dfs for each
            for pre_req in course_dep[crs]:
                # if any of the deps return False, we know we cannot schedule
                if not dfs(pre_req): return False
                
            # if we are here, we know that we can visit all deps of current crs
            # so we remove it from visited for next iteration
            # and we set the deps to [], since we can visit it
            ## BACKTRACKING
            visited.remove(crs)
            course_dep[pre_req] = []
            
            return True
                    
        # need to do it for every course, because we can have unconnected graphs    
        for crs in course_dep:
            if not dfs(crs): return False
        
        return True