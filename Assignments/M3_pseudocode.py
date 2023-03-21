employee_wage = 20
hours_worked = float(input('Total hours worked? '))

regular_pay = employee_wage * hours_worked
overtime_hours = 0

if hours_worked > 40:
    overtime_hours = hours_worked % 40

overtime_pay = overtime_hours * (employee_wage * 1.5)
total_pay  = '%.2f' % (regular_pay + overtime_pay)
print(f'Total pay: ${total_pay}')
