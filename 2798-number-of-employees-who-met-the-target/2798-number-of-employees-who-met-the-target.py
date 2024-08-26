class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        counter = 0
        for emp_hour in hours:
            if emp_hour >= target:
                counter +=1
                
        return counter