# Conditional statements in python
from pyscript import document, display #type:ignore


def student_information(e):
    document.getElementById('output').innerHTML=""
    output = document.getElementById('output')
    output.innerHTML = ""   # clear previous
    Last_Name= document.getElementById('Last_Name').value
    First_Name= document.getElementById('First_Name').value
    Gr1= int(document.getElementById('SCARING101').value)
    Gr2= int(document.getElementById('ABM').value)
    Gr3= int(document.getElementById('TECH').value)
    Gr4= int(document.getElementById('LIBARTS').value)
    Gr5= int(document.getElementById('STEM').value)
    Gr6= int(document.getElementById('ENGLISH').value)
    grades= (Gr1, Gr2, Gr3, Gr4, Gr5, Gr6)
    units = (5, 2, 3, 1, 2, 3)
    grade1 = (grades[0] * units [5])
    grade2 = (grades[1] * units [1])
    grade3 = (grades[2] * units [3])
    grade4 = (grades[3] * units [2])
    grade5 = (grades[4] * units [2])
    grade6 = (grades[5] * units [5])

    total_sum= grade1 + grade2 + grade3 + grade4 + grade5 + grade6
    total_value = (units [0] * 3) + (units [1] * 1) + (units [2] * 1) + (units [3] * 1)
    fg = total_sum / total_value

# Displaying student grades

    display(f'SCARING101: {Gr1} ', target='output')
    display(f'ABM: {Gr2} ', target='output')
    display(f'TECH: {Gr3} ', target='output')
    display(f'LIBARTS: {Gr4} ', target='output')
    display(f'STEM: {Gr5} ', target='output')
    display(f'ENGLISH: {Gr6} ', target='output')
    display(f'{Last_Name} {First_Name}', target='output')
    display(f'Your final grade is {fg}', target='output')


def number_checker(e):
  num1 = int(document.getElementById('input1').value)

if >= 75 :
  display(f'You Passed!', target='output')
else:
  display(f'You Failed..', target='output')
