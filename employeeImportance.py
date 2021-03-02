# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
from collections import defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empImport = [0]
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id] = (emp.subordinates,emp.importance)
        return self.Helper(graph,id,empImport)
    def Helper(self,graph,id,empImport):
        empImport[0] += graph[id][1]
        for subord in graph[id][0]:
            self.Helper(graph,subord,empImport)
        return empImport[0]
            
            
            
            
            
#         empImportance = [0]
#         return self.Helper(employees,empImportance,id)
#     def Helper(self,employees,empImportance,id):
#         for employee in employees:     
#             if employee.id == id:
#                 empImportance[0] += employee.importance
#                 while employee.subordinates:
#                     subordinate = employee.subordinates.pop()
#                     self.Helper(employees,empImportance,subordinate)
#         return empImportance[0]
            
            
        