
###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import kayboard # your own defined module

# Reads employee's data from keyboard
first_name = kayboard.input_string('Enter name: ')
last_name = kayboard.input_string('Enter surname: ')
age = kayboard.input_integer('Enter age: ')
salary = kayboard.input_real('Enter salary: ')
is_salary_hidden = kayboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname:', last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary', salary)
