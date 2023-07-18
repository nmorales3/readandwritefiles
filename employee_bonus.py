import csv

employee= open('EmployeePay.csv','r')

employee_file=csv.reader(employee, delimiter=',')

next(employee_file)

for record in employee_file:
    print(record)

    print('Employee First Name:', record[1])
    print('Employee Last Name:', record[2])
    print('Salary:', record[3])
    record[3]=float(record[3])
    record[4]=float(record[4])
   
    print('Bonus:', record[3]*record[4])

input()