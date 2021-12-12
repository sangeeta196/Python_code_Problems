
"""Problem_1.ipynb : 
Write a program in Python to prompt the user to input their name, employee number, week ending date, hours worked, rate per hour, standard and overtime tax percentage rate. 
Use the data input to calculate gross pay, tax deductions and net pay. Output the results as a formatted payslip. Assume that a standard working week is 37.5 hours.


Original file is located at
    https://github.com/sangeeta196/Python_code_Problems.git
"""

###Collect details from the data and store it###

employee_name=input('Enter Employee name: ')
employee_number=int(input('Enter Employee number: '))
week_ending=(input('Enter date of week ending(dd/mm/yyyy): '))
work_hrs=float(input('Enter Number of hours worked: '))
a=float(input('Enter the overtime rate: '))
hr_rate=float(input('Enter the standard hourly rate for the payslip: '))
overtime_rate=hr_rate*a
std_tax_rate=float(input('Enter standard tax rate: '))
overtime_tax_rate=float(input('Enter overtime tax rate: '))
std_hrs=37.5  #Standard working hrs


###if number of working hours is  less <= to  standard hours then overtime hours is zero###
if(work_hrs<=std_hrs):
    normal_hrs=work_hrs
    normal_hrs_pay =work_hrs*hr_rate
    overtime_hrs_pay=0
    overtime_hrs=0

else:
    overtime_hrs = work_hrs - std_hrs
    normal_hrs=std_hrs
    normal_hrs_pay=normal_hrs*hr_rate
    overtime_hrs_pay=overtime_hrs*overtime_rate*hr_rate

###Calculation of tax for normal hrs###

normal_hrs_tax=(normal_hrs_pay*std_tax_rate)/100

###Calculation of tax for over time hrs###

overtime_tax=(overtime_hrs_pay*overtime_tax_rate)/100

###Total pay is the sum of normal hours pay and over time hours pay###

total_pay=normal_hrs_pay+overtime_hrs_pay
###total deduction is the sum of normal hours tax and over time hours tax rate###

total_deduction=normal_hrs_tax+overtime_tax_rate

### net pay is the difference between total pay and total deduction###
net_pay=total_pay-total_deduction

### printing pay slip###

print("\t\t\tP A Y S L I P")
print("Week Ending: "+week_ending)
print("Employee: " +employee_name)
print("Employee Number: " +str(employee_number))
print("\t\t\t"+"Earnings"+"\t\t"+"Deductions"+"\n"+"\t\t"+"Hours"+"\t"+"Rate"+"\t"+"Total"+"\n"+"Hours(normal)"+"\t"+str(normal_hrs)+"\t"+str(hr_rate)
        +"\t"+str(round(normal_hrs_pay,2))+"\t"+" Tax @  " +str(std_tax_rate)+" "+"%"+"\t"+str(round(normal_hrs_tax,2))+"\n"+ "Hours(overtime)"+"\t"+
        str(overtime_hrs)+"\t"+str(round(overtime_hrs,2))+"\t"+str(round(overtime_hrs_pay,2))+"\t"+" Tax @  "+str(overtime_tax_rate)+" %"+"\t"+str(overtime_tax_rate))
print('                                                                                  ')
print("\t\t"+"Total Pay: "+"\t\t\t\t"+str(round(total_pay,2)))
print("\t\t"+"Total Deduction: "+"\t\t\t"+str(round(total_deduction,2)))
print("\t\t"+"Net Pay: "+"\t\t\t\t"+str(round(net_pay,2)))