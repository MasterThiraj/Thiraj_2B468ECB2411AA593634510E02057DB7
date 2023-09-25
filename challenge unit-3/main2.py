'''
Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
'''
class Student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,key=lambda CGPA_Number: CGPA_Number.cgpa,reverse = True)
 
  return sorted_students

#Example usage:
students = [
  Student("Hari","A122", 7.8),Student("Srikanth","A123", 8.9),Student("Master Thiraj","A124", 9.9),Student("Karthi","A125",9.8)
]

sorted_students = sort_students(students)

#print the sorted list of students
for CGPA_Number in sorted_students:
  print(f"Name:{CGPA_Number.name}\n Roll_Number:{CGPA_Number.roll_number}\n CGPA:{CGPA_Number.cgpa}.")