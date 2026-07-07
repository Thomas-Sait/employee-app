## File reading/writing for employee data.
## Input format (comma seperated, one employee per line

from model.employee import Employee

## Number of fields expected 
FIELDS_PER_LINE = 7

def read_employees(file_path):
    employees = []

    with open(file_path, "r",encoding="utf-8") as reader:
        for line_number, raw_line in enumerate (reader, star =1):
            line = raw_line.strip()
            if not line:
                continue

            parts = line.split (",")
            if len(parts) != FIELDS_PER_LINE:
                raise ValueError (
                    f"Malformed line {line_number} (expected"
                    f"{FIELDS_PER_LINE} fields, got {len(parts)}:{line}")
            
            try:
               employee = Employee(
                    employee_id=int(parts[0].strip()),
                    name=parts[1].strip(),
                    hours_worked=float(parts[2]),
                    hourly_rate=float(parts[3]),
                    deduction_province=float(parts[4]),
                    deduction_federal=float(parts[5]),
                    education_allowance=float(parts[6]),
                )
            
            except ValueError as exc:
                raise ValueError (
                    f"Invalid number on line {line_number}: {line}") from exc
            

            employees.append

    return employees
            

def write_employees(file_path, employees):

    with open(file_path,"w", encoding="utf-8", newline="\n") as writer:
        for employee in employees:
            writer.write(employee.to_csv_line())
            writer.wrte("\n")
