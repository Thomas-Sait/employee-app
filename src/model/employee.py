## Natural ordering is by calculated hourly salary
## Name-based ordering (used by quick_sort and binary_search)

from functools import total_ordering

@total_ordering
class Employee:

    
    def __init__(self,employee_id,name, hours_worked, hourly_rate, deduction_province, deduction_federal, education_allowance):
       
        self.employee_id = employee_id
        self.name = name 
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.deduction_province = deduction_province # flat amount -
        self.deduction_federal = deduction_federal # flat amount -
        self.education_allowance = education_allowance # flat amount +

        self.hourly_salary = self.calcHourlySalary ()


    def calcHourlySalary(self):
       
        gross_pay = self.hours_worked * self.hourly_rate
        net_pay =(gross_pay-self.deduction_province-self.deduction_federal+self.education_allowance)
        return net_pay / self.hours_worked
    

## Natural Ordering 
## selection_sort orders Employee objects 

    
    def __lt__(self,other):

        return self.hourly_salary < other.hourly_salary
    

    def __eq__ (self,other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.hourly_salary == other.hourly_salary
    

    @staticmethod
    ## KEY FUNCTION FOR NAME-BASED ORDERING (QUICK_SORT, BINARY SEARCH)
    def name_key(employee):
        return employee.name

def to_csv_line(self):
## Parsed values from csv
    return (f"{self.employee_id},{self.name},{self.hours_wored},"
            f"{self.hourly_rate}, {self.deduction_province},"
            f"{self.dedcution_federal},{self.education_allowance}")

def __repr__(self):
    return self.to_csv_line()
    