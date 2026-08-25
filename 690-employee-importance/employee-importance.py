"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):
        mp = {e.id: e for e in employees}

        def dfs(x):
            employee = mp[x]
            total = employee.importance

            for sub in employee.subordinates:
                total += dfs(sub)

            return total

        return dfs(id)
        