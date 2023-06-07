#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (45.43%)
# Likes:    13497
# Dislikes: 542
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # define graph and indegree
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # construct the graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        print(graph)
        # BFS - queue will contain the courses that have no prerequisites
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            # remove a course from queue
            node = queue.pop(0)
            
            # decrease indegree for next courses
            for next_course in graph[node]:
                indegree[next_course] -= 1
                # if next course has no more prerequisites, add it to queue
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        # if all courses could be taken, return True
        return not any(indegree)


        
# @lc code=end

